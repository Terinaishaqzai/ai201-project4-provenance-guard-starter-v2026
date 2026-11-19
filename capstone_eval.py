#!/usr/bin/env python3
"""
Capstone evaluation — my five capstone criteria (criteria.md, ## Capstone).
Three trials each, nothing changed between trials.

    python capstone_eval.py --label before            criteria 1, 2, 3, 5 (+ 4 if run)
    python capstone_eval.py --crit4 torch --label before
    python capstone_eval.py --crit4 model --label before
    python capstone_eval.py --cost                     cost of one run

Needs the service running. Every request uses its own creator_id, so the
10/minute per-creator rate limit never trips during a run.

  Criterion 1  10 invalid texts (INVALID_TEXTS) -> each must be 400 + JSON error,
               with no guess or label.
  Criterion 2  The same 10 refused requests -> each must have an entry in the
               audit log with its creator_id and status "rejected".
  Criterion 3  10 short sentences from my own essay, 8-20 words (SHORT_HUMAN)
               -> at least 9 must be 200 with confidence and label.
  Criterion 4  Run separately, because it needs the server restarted broken:
                 torch:  python run_without_torch.py
                 model:  AI201_DETECTOR_MODEL=no-such-model-capstone python app.py
               then --crit4 torch / --crit4 model. Each sends 3 trials of one
               valid text, which must get 503 + JSON error, no label, and a
               model_unavailable entry in the log.
  Criterion 5  The 20 requests from criteria 1 and 3 -> each log record must have
               duration_ms >= 0 and text_chars == len(text).

Writes results/capstone_<label>_<timestamp>.md (+ .json).
"""

import argparse
import glob
import json
import os
import uuid
import urllib.error
import urllib.request
from datetime import datetime

import config

BASE = f"http://127.0.0.1:{config.PORT}"
RESULTS = str(config.RESULTS_DIR)

# Criterion 1: fixed before any results. Single characters, punctuation only,
# emoji, and random keyboard characters.
INVALID_TEXTS = [
    "a",                       # single character
    "?",                       # single character
    "!!! ??? ... ,,,",         # punctuation only
    "-- ;; :: ** //",          # punctuation only
    "🙂🙃😀😃😄😁",              # emoji only
    "🔥🔥🔥 💯💯 👍",            # emoji only
    "asdfghjkl",               # keyboard characters, one run
    "qwe rty uio",             # keyboard characters, spaced
    "#$%^&*()_+",              # keyboard symbols
    "zxcvbnm,./ asdf",         # keyboard characters and symbols
]

# Criterion 3: sentences of 8-20 words taken from my own essay, "A World
# Connected" (the human samples in scenarios.py, written without AI).
SHORT_HUMAN = [
    "By the seventeenth and eighteenth centuries, globalization expanded dramatically in both geographic scope and coercive character.",
    "These commodities generated enormous profits and transformed European society; sugar reshaped diets, and coffeehouses became centers of commercial life.",
    "During the nineteenth century, industrialization gave Western nations unprecedented advantages that they used to reshape the global order through imperialism.",
    "This asymmetry would define global economic relationships well into the twentieth century.",
    "The two World Wars simultaneously devastated and deepened global interconnectedness.",
    "After 1945, institutions like the United Nations and the World Bank were founded to manage global interdependence through multilateral cooperation.",
    "The Cold War then extended integration through superpower competition.",
    "Between 1950 and 2000, technology and transnational corporations became the twin engines of an accelerating globalization.",
    "The digital revolution had made the world smaller without making it more equal.",
    "Each era intensified the world's interconnectedness, and each era reproduced the inequality that has always accompanied it.",
]

CRIT4_TEXT = "The two World Wars simultaneously devastated and deepened global interconnectedness."


def post(path, data):
    req = urllib.request.Request(BASE + path, data=json.dumps(data).encode(), method="POST",
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


def creator(tag, label, trial, i):
    return f"cap_{label}_t{trial}_{tag}{i:02d}_{uuid.uuid4().hex[:6]}"


def is_json_error(body):
    return isinstance(body, dict) and "error" in body and "guess" not in body and "label" not in body


def run_trial(label, trial):
    sent = []   # (criterion, creator_id, text, status, body)
    for i, text in enumerate(INVALID_TEXTS, 1):
        cid = creator("inv", label, trial, i)
        status, body = post("/submit", {"text": text, "creator_id": cid})
        sent.append(("c1", cid, text, status, body))
    for i, text in enumerate(SHORT_HUMAN, 1):
        cid = creator("hum", label, trial, i)
        status, body = post("/submit", {"text": text, "creator_id": cid})
        sent.append(("c3", cid, text, status, body))

    log = get_log()
    by_creator = {}
    for e in log:
        by_creator.setdefault(e.get("creator_id"), []).append(e)

    c1 = [s for s in sent if s[0] == "c1"]
    c3 = [s for s in sent if s[0] == "c3"]

    c1_pass = [s[3] == 400 and is_json_error(s[4]) for s in c1]
    c2_pass = [any(e.get("status") == "rejected" for e in by_creator.get(s[1], [])) for s in c1]
    c3_pass = [s[3] == 200 and isinstance(s[4], dict) and "confidence" in s[4] and "label" in s[4]
               for s in c3]

    c5_pass = []
    for s in sent:
        entries = by_creator.get(s[1], [])
        e = entries[-1] if entries else {}
        d = e.get("duration_ms")
        ok = (isinstance(d, (int, float)) and not isinstance(d, bool) and d >= 0
              and e.get("text_chars") == len(s[2]))
        c5_pass.append(ok)

    rows = []
    for s, p1, p2 in zip(c1, c1_pass, c2_pass):
        rows.append({"criterion": "1+2", "creator_id": s[1], "sent": s[2], "status": s[3],
                     "response": s[4], "c1_pass": p1, "c2_pass": p2,
                     "log": by_creator.get(s[1], [])})
    for s, p3 in zip(c3, c3_pass):
        rows.append({"criterion": "3", "creator_id": s[1], "sent": s[2], "status": s[3],
                     "response": s[4], "c3_pass": p3, "log": by_creator.get(s[1], [])})
    for r, p5 in zip(rows, c5_pass):
        r["c5_pass"] = p5

    return {
        "trial": trial,
        "c1": sum(c1_pass), "c2": sum(c2_pass), "c3": sum(c3_pass), "c5": sum(c5_pass),
        "rows": rows,
    }


def crit4(scenario, label):
    trials = []
    for t in (1, 2, 3):
        cid = creator(f"c4{scenario}", label, t, 1)
        status, body = post("/submit", {"text": CRIT4_TEXT, "creator_id": cid})
        entries = [e for e in get_log() if e.get("creator_id") == cid]
        logged = any(e.get("reason") == "model_unavailable" for e in entries)
        ok = status == 503 and is_json_error(body) and logged
        trials.append({"trial": t, "status": status, "response": body, "log": entries, "pass": ok})
        print(f"  trial {t}: {status} {body}  logged={logged}  -> {'PASS' if ok else 'FAIL'}")
    os.makedirs(RESULTS, exist_ok=True)
    path = os.path.join(RESULTS, f"capstone_crit4_{scenario}_{label}_{datetime.now():%Y-%m-%d_%H%M}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"scenario": scenario, "label": label, "trials": trials}, f, indent=2, ensure_ascii=False)
    print(f"wrote {path}")


def latest_crit4(scenario, label):
    files = sorted(glob.glob(os.path.join(RESULTS, f"capstone_crit4_{scenario}_{label}_*.json")))
    if not files:
        return None
    with open(files[-1], encoding="utf-8") as f:
        return json.load(f)


def verdict(counts, target):
    return "MET" if all(c >= target for c in counts) else "MISSED"


def report(label, trials):
    c = {k: [t[k] for t in trials] for k in ("c1", "c2", "c3", "c5")}
    torch_r, model_r = latest_crit4("torch", label), latest_crit4("model", label)
    if torch_r and model_r:
        c4 = [int(torch_r["trials"][i]["pass"]) + int(model_r["trials"][i]["pass"]) for i in range(3)]
        c4_cells = [f"{n}/2" for n in c4]
        c4_verdict = verdict(c4, 2)
    else:
        c4, c4_cells, c4_verdict = None, ["not run"] * 3, "NOT RUN"

    lines = [
        f"# Capstone run log: {label}",
        "",
        f"Run {datetime.now():%Y-%m-%d %H:%M} with `python capstone_eval.py --label {label}`.",
        "",
        "| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |",
        "|---|---|---|---|---|---|",
        f"| 1. Invalid text refused with 400 + JSON error | 10 of 10 | "
        + " | ".join(f"{n}/10" for n in c["c1"]) + f" | {verdict(c['c1'], 10)} |",
        f"| 2. Every refused request in the audit log | 10 of 10 | "
        + " | ".join(f"{n}/10" for n in c["c2"]) + f" | {verdict(c['c2'], 10)} |",
        f"| 3. Short human writing accepted and scored | at least 9 of 10 | "
        + " | ".join(f"{n}/10" for n in c["c3"]) + f" | {verdict(c['c3'], 9)} |",
        f"| 4. Missing torch / missing GPT-2 return 503 | 2 of 2 | "
        + " | ".join(c4_cells) + f" | {c4_verdict} |",
        f"| 5. duration_ms and text_chars in every record | 20 of 20 | "
        + " | ".join(f"{n}/20" for n in c["c5"]) + f" | {verdict(c['c5'], 20)} |",
        "",
    ]

    failures = [(t["trial"], r) for t in trials for r in t["rows"]
                if not all(r.get(k, True) for k in ("c1_pass", "c2_pass", "c3_pass", "c5_pass"))]
    lines += ["## Requests that failed a criterion", ""]
    if failures:
        lines.append("```json")
        for trial, r in failures:
            lines.append(json.dumps({"trial": trial, "sent": r["sent"], "status": r["status"],
                                     "response": r["response"],
                                     "failed": [k for k in ("c1_pass", "c2_pass", "c3_pass", "c5_pass")
                                                if r.get(k) is False],
                                     "log": r["log"]}, ensure_ascii=False))
        lines.append("```")
    else:
        lines.append("None.")
    lines.append("")

    t1 = trials[0]["rows"]
    lines += ["## Real output, trial 1 (`capstone_eval.py::run_trial`)", "", "```json"]
    for r in t1:
        lines.append(json.dumps({"criterion": r["criterion"], "sent": r["sent"], "status": r["status"],
                                 "response": r["response"]}, ensure_ascii=False))
    lines += ["```", "", "## Audit log records for trial 1 (`logs/audit.jsonl`)", "", "```json"]
    for r in t1:
        for e in r["log"]:
            lines.append(json.dumps(e, ensure_ascii=False))
    lines += ["```", ""]

    if torch_r and model_r:
        lines += ["## Criterion 4 output (`capstone_eval.py::crit4`)", "", "```json"]
        for r in (torch_r, model_r):
            t = r["trials"][0]
            lines.append(json.dumps({"scenario": r["scenario"], "status": t["status"],
                                     "response": t["response"], "log": t["log"]}, ensure_ascii=False))
        lines += ["```", ""]

    os.makedirs(RESULTS, exist_ok=True)
    stem = os.path.join(RESULTS, f"capstone_{label}_{datetime.now():%Y-%m-%d_%H%M}")
    with open(stem + ".md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    with open(stem + ".json", "w", encoding="utf-8") as f:
        json.dump({"label": label, "trials": trials}, f, indent=2, ensure_ascii=False)
    print("\n".join(lines[4:11]))
    print(f"\nwrote {stem}.md and {stem}.json")


def cost():
    import scenarios
    texts = scenarios.SCENARIOS[0]["texts"]   # my own essay paragraphs: normal-size submissions
    print("warm-up request (loads the model if this server hasn't yet)...")
    warm_cid = f"cap_cost_warmup_{uuid.uuid4().hex[:6]}"
    post("/submit", {"text": texts[0], "creator_id": warm_cid})
    cids = []
    for i, text in enumerate(texts, 1):
        cid = f"cap_cost_{i:02d}_{uuid.uuid4().hex[:6]}"
        status, _ = post("/submit", {"text": text, "creator_id": cid})
        cids.append(cid)
        print(f"  run {i}: {status}")
    log = get_log()
    warm = [e["duration_ms"] for e in log if e.get("creator_id") == warm_cid and "duration_ms" in e]
    ds = [e["duration_ms"] for e in log if e.get("creator_id") in cids and "duration_ms" in e]
    avg = sum(ds) / len(ds)
    per_day_s = avg / 1000 * 100
    lines = [
        "# Capstone cost measurement",
        "",
        f"Run {datetime.now():%Y-%m-%d %H:%M} with `python capstone_eval.py --cost`.",
        "Cost is seconds of compute: `duration_ms` from `/submit`'s own audit records,",
        f"over {len(ds)} warm submissions of my essay paragraphs (after one warm-up).",
        "",
        f"- Warm-up request: {warm[0] if warm else 'n/a'} ms",
        f"- Per run: average {avg:.1f} ms, min {min(ds):.1f} ms, max {max(ds):.1f} ms",
        f"- All runs (ms): {', '.join(f'{d:.1f}' for d in ds)}",
        f"- 100 people a day, one submission each: {avg:.1f} ms x 100 = {per_day_s:.1f} s of compute a day",
        "",
    ]
    os.makedirs(RESULTS, exist_ok=True)
    path = os.path.join(RESULTS, f"capstone_cost_{datetime.now():%Y-%m-%d_%H%M}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("\n".join(lines))
    print(f"wrote {path}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--label", default="before")
    p.add_argument("--crit4", choices=["torch", "model"])
    p.add_argument("--cost", action="store_true")
    a = p.parse_args()
    if a.cost:
        cost()
    elif a.crit4:
        print(f"criterion 4, scenario {a.crit4}, label {a.label}")
        crit4(a.crit4, a.label)
    else:
        trials = []
        for t in (1, 2, 3):
            print(f"trial {t}...")
            trials.append(run_trial(a.label, t))
        report(a.label, trials)


if __name__ == "__main__":
    main()
