#!/usr/bin/env python3
"""
The parts of my evaluation that scenarios.py can't express. Three trials each.

    python eval_extra.py --label before

  Criterion 3  Label coverage: scoring.score_to_label at 0.20 / 0.50 / 0.90, plus a
               sweep of every score from 0.000 to 1.000 (step 0.001) checking each
               maps to exactly one of the three labels.
  Criterion 4  Appeal handling: 5 submissions -> 5 appeals -> check each appeal
               returns 200 and the audit log shows status under_review; plus one
               appeal with an unknown content_id, which must return 404.
  Criterion 5  (5th case) A JSON body that is not an object must return 400.

Needs the service running (python app.py) for criteria 4 and 5.
Writes results/eval_extra_<label>_<timestamp>.json
"""

import argparse
import json
import uuid
import urllib.error
import urllib.request
from datetime import datetime

import config
import scoring

BASE = f"http://127.0.0.1:{config.PORT}"
VALID = {"human", "unsure", "ai"}

APPEAL_TEXTS = [
    "I spent most of last weekend rebuilding the shelf in my closet. The old brackets had bent, so everything kept sliding to one side. I measured twice, drilled once, and still got one hole slightly off. It holds now, though, and that is what counts.",
    "Our team meeting ran long because nobody could agree on the deadline. Two people wanted Friday, one wanted Monday, and I just wanted to go home. We settled on Monday morning. I already know I will be finishing it Sunday night.",
    "The bus was twenty minutes late again today. I used the time to read a few pages of the book I keep meaning to finish. By the time the bus came, I had forgotten I was annoyed. Maybe late buses are underrated.",
    "My grandmother taught me to make bread without measuring anything. She would just look at the dough and know. I measure everything and it still comes out flat half the time. I think the secret is mostly patience.",
    "I tried a new route on my morning run and got completely lost. Thirty minutes later I was back on a street I recognized. My watch said I had run twice my usual distance. My legs agreed with the watch.",
]


def post(path, data=None, raw=None):
    body = raw.encode() if raw is not None else json.dumps(data).encode()
    req = urllib.request.Request(BASE + path, data=body, method="POST",
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as r:
            return r.status, json.loads(r.read() or b"null")
    except urllib.error.HTTPError as e:
        txt = e.read()
        try:
            return e.code, json.loads(txt)
        except Exception:
            return e.code, txt.decode(errors="replace")[:200]


def get_log():
    with urllib.request.urlopen(BASE + "/log") as r:
        return json.loads(r.read())["entries"]


def criterion_3():
    spot = {s: scoring.score_to_label(s)[0] for s in (0.20, 0.50, 0.90)}
    spot_ok = spot == {0.20: "human", 0.50: "unsure", 0.90: "ai"}
    bad = []
    for i in range(0, 1001):
        s = i / 1000
        try:
            guess = scoring.score_to_label(s)[0]
            if guess not in VALID:
                bad.append((s, guess))
        except Exception as exc:
            bad.append((s, repr(exc)))
    return {
        "spot_checks": {str(k): v for k, v in spot.items()},
        "spot_checks_passed": f"{sum(spot[k] == v for k, v in {0.20: 'human', 0.50: 'unsure', 0.90: 'ai'}.items())}/3",
        "sweep_scores_checked": 1001,
        "sweep_failures": bad[:10],
        "sweep_passed": not bad,
        "pass": spot_ok and not bad,
    }


def criterion_4(trial):
    results = []
    for i, text in enumerate(APPEAL_TEXTS, 1):
        creator = f"eval_appeal_t{trial}_{i}_{uuid.uuid4().hex[:6]}"
        s_status, s_body = post("/submit", {"text": text, "creator_id": creator})
        cid = s_body.get("content_id") if isinstance(s_body, dict) else None
        a_status, a_body = (None, None)
        if cid:
            a_status, a_body = post("/appeal", {"content_id": cid,
                                                "reasoning": "I wrote this myself."})
        results.append({"submit_status": s_status, "content_id": cid,
                        "appeal_status": a_status, "appeal_response": a_body})

    log = get_log()
    for r in results:
        r["logged_under_review"] = any(
            e.get("content_id") == r["content_id"] and e.get("status") == "under_review"
            for e in log
        ) if r["content_id"] else False
        r["pass"] = r["appeal_status"] == 200 and r["logged_under_review"]

    unknown_status, unknown_body = post("/appeal", {
        "content_id": f"does-not-exist-{uuid.uuid4()}",
        "reasoning": "testing an unknown id"})
    passed = sum(r["pass"] for r in results)
    return {
        "valid_appeals": results,
        "valid_appeals_passed": f"{passed}/5",
        "unknown_id_status": unknown_status,
        "unknown_id_response": unknown_body,
        "pass": passed == 5 and unknown_status == 404,
    }


def criterion_5_non_object():
    status, body = post("/submit", raw='["not", "an", "object"]')
    return {"case": "JSON body is a list, not an object",
            "status": status, "response": body, "pass": status == 400}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", default="run")
    args = ap.parse_args()

    trials = []
    for t in (1, 2, 3):
        print(f"Trial {t}...")
        c3, c4, c5 = criterion_3(), criterion_4(t), criterion_5_non_object()
        print(f"  C3 label coverage: spot {c3['spot_checks_passed']}, "
              f"sweep {'ok' if c3['sweep_passed'] else 'FAILED'}")
        print(f"  C4 appeals: {c4['valid_appeals_passed']} valid, "
              f"unknown id -> {c4['unknown_id_status']}")
        print(f"  C5 non-object body -> {c5['status']}")
        trials.append({"trial": t, "criterion_3": c3, "criterion_4": c4,
                       "criterion_5_non_object": c5})

    stamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    out = config.RESULTS_DIR / f"eval_extra_{args.label}_{stamp}.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(trials, indent=2))
    print(f"\nWrote {out}")


if __name__ == "__main__":
    main()