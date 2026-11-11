# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 16:49
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `21c9283e-883f-4537-8783-f224c4937e2e` | unsure | 0.245 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `381d89af-e333-4ab0-b703-c79d90a76af4` | unsure | 0.197 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `25b52a65-d492-4f01-a9c9-5d64447de26c` | unsure | 0.081 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `f35e686f-1518-4320-8177-ddfc937e9899` | unsure | 0.183 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `f084e8ae-c6d0-4cbd-adf9-238311537e00` | human | 0.417 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `2b071601-3ccf-4b5d-905d-591ab12c013e` | unsure | 0.185 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `73149403-7a89-4028-afaa-47c900bc2867` | unsure | 0.096 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `1369ea8f-b68d-4f54-9fb3-70afb4d1dfac` | unsure | 0.232 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `68b6c771-b65d-45a6-bb45-3fae26e59b2e` | unsure | 0.104 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `af66e323-bf47-4d04-9689-f58b5f8621e3` | ai | 0.637 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `cd3f4090-1af4-4427-bade-1bdf926e80d9` | unsure | 0.100 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `04776013-577b-4415-a270-f17b5ccca4ea` | unsure | 0.362 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `a4473476-a71e-49e1-8966-25bd475c4adb` | unsure | 0.383 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `828ab89d-aead-473c-8387-86b2c47c3e40` | unsure | 0.346 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `baf262db-7a5c-494c-825e-33e27d17fbd6` | ai | 0.423 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `4a73f270-03aa-4d03-8fdd-c6a6f98329d9` | unsure | 0.321 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `b9fef2bf-3174-458f-9f5e-909bce0cdda5` | unsure | 0.254 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `5710ab09-b43c-42ec-8e7d-14819ac294d3` | unsure | 0.248 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `466f53b6-c0c9-4657-9c75-157cc04b06ad` | unsure | 0.232 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `f8e31cfd-39b6-4bf9-8271-2ea6247ae558` | human | 0.534 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `c31b8a12-1e7f-4fe7-96d3-20abb2710d88` | unsure | 0.089 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `d5c3a921-62b1-498d-acce-6c30456e24c4` | unsure | 0.046 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `a46f8f4f-0318-45a8-b58a-a3140002c67c` | unsure | 0.144 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `926126f4-bda0-419b-8786-da2485c03569` | unsure | 0.050 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `9a251edf-fbc9-422e-b90a-3d890a025d68` | human | 0.550 |  |
| MF04 | malformed | text is only punctuation | 200 | `db585a99-e321-462a-a2ce-ed616ba5c0d2` | human | 0.489 |  |
| MF05 | malformed | text is a very long single word | 200 | `058bf625-f49c-4d09-9d40-e02c8ead1c73` | ai | 0.448 |  |
| MF06 | malformed | text is emoji only | 200 | `28d2febe-b049-4322-87c4-79e188e51270` | ai | 0.497 |  |
| MF07 | malformed | text is right-to-left script | 200 | `ca92315a-2a95-4984-b77b-3e9b10e4cff4` | ai | 0.406 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `c0802276-c184-4317-a0eb-ad7f08a0f833` | ai | 0.699 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `26f40403-dcad-4954-87e9-55470032396e` | human | 0.521 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3eb9c09b-5fed-438b-b5a5-836e1cc05d5e` | human | 0.521 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7c7549d0-db85-49c5-b3cb-05e9c414026b` | human | 0.521 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2499ca6a-9f3a-40cc-9b6b-75840625c370` | human | 0.521 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fb668e1f-04a8-4068-8662-b385d89b8922` | human | 0.521 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2a5751a3-25ce-4c19-9b37-905cc1070cf5` | human | 0.521 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1cc89afc-9225-4285-9c94-35640c10d28c` | human | 0.521 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3f2253eb-508d-48bd-a963-0f03adcd4198` | human | 0.521 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `beda4f26-ba24-4a12-b08d-eb5102e15524` | human | 0.521 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `869a5761-3e3c-4e6e-a003-36935d2818fb` | human | 0.521 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "21c9283e-883f-4537-8783-f224c4937e2e",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.2452,
  "model_score": 0.1635,
  "style_score": 0.5913,
  "label": "We cannot confidently determine whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "381d89af-e333-4ab0-b703-c79d90a76af4",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.1969,
  "model_score": 0.5943,
  "style_score": 0.2088,
  "label": "We cannot confidently determine whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "25b52a65-d492-4f01-a9c9-5d64447de26c",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.0806,
  "model_score": 0.6662,
  "style_score": 0.4144,
  "label": "We cannot confidently determine whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "f35e686f-1518-4320-8177-ddfc937e9899",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.1829,
  "model_score": 0.6114,
  "style_score": 0.5715,
  "label": "We cannot confidently determine whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "f084e8ae-c6d0-4cbd-adf9-238311537e00",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.4167,
  "model_score": 0.3212,
  "style_score": 0.2621,
  "label": "This writing shows patterns associated with human-written text.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "2b071601-3ccf-4b5d-905d-591ab12c013e",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.1849,
  "model_score": 0.5727,
  "style_score": 0.2424,
  "label": "We cannot confidently determine whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "73149403-7a89-4028-afaa-47c900bc2867",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.0958,
  "model_score": 0.5862,
  "style_score": 0.318,
  "label": "We cannot confidently determine whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "1369ea8f-b68d-4f54-9fb3-70afb4d1dfac",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.2316,
  "model_score": 0.2452,
  "style_score": 0.5232,
  "label": "We cannot confidently determine whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "68b6c771-b65d-45a6-bb45-3fae26e59b2e",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.1039,
  "model_score": 0.7042,
  "style_score": 0.3997,
  "label": "We cannot confidently determine whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "af66e323-bf47-4d04-9689-f58b5f8621e3",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.6369,
  "model_score": 0.9792,
  "style_score": 0.6577,
  "label": "This writing shows patterns associated with AI-generated text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "cd3f4090-1af4-4427-bade-1bdf926e80d9",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.0995,
  "model_score": 0.6175,
  "style_score": 0.482,
  "label": "We cannot confidently determine whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "04776013-577b-4415-a270-f17b5ccca4ea",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.3622,
  "model_score": 0.7387,
  "style_score": 0.6235,
  "label": "We cannot confidently determine whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "a4473476-a71e-49e1-8966-25bd475c4adb",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.3831,
  "model_score": 0.8051,
  "style_score": 0.578,
  "label": "We cannot confidently determine whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "828ab89d-aead-473c-8387-86b2c47c3e40",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.3464,
  "model_score": 0.8329,
  "style_score": 0.5135,
  "label": "We cannot confidently determine whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "baf262db-7a5c-494c-825e-33e27d17fbd6",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.4232,
  "model_score": 0.8005,
  "style_score": 0.6227,
  "label": "This writing shows patterns associated with AI-generated text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "4a73f270-03aa-4d03-8fdd-c6a6f98329d9",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.321,
  "model_score": 0.8814,
  "style_score": 0.4396,
  "label": "We cannot confidently determine whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "b9fef2bf-3174-458f-9f5e-909bce0cdda5",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.2536,
  "model_score": 0.8816,
  "style_score": 0.372,
  "label": "We cannot confidently determine whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "5710ab09-b43c-42ec-8e7d-14819ac294d3",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.2483,
  "model_score": 0.3223,
  "style_score": 0.4294,
  "label": "We cannot confidently determine whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "466f53b6-c0c9-4657-9c75-157cc04b06ad",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.2317,
  "model_score": 0.4625,
  "style_score": 0.3058,
  "label": "We cannot confidently determine whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "f8e31cfd-39b6-4bf9-8271-2ea6247ae558",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.5341,
  "model_score": 0.2044,
  "style_score": 0.2615,
  "label": "This writing shows patterns associated with human-written text.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "c31b8a12-1e7f-4fe7-96d3-20abb2710d88",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.089,
  "model_score": 0.5943,
  "style_score": 0.4947,
  "label": "We cannot confidently determine whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "d5c3a921-62b1-498d-acce-6c30456e24c4",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.0462,
  "model_score": 0.4998,
  "style_score": 0.454,
  "label": "We cannot confidently determine whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "a46f8f4f-0318-45a8-b58a-a3140002c67c",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.1445,
  "model_score": 0.6401,
  "style_score": 0.2154,
  "label": "We cannot confidently determine whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "926126f4-bda0-419b-8786-da2485c03569",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.0498,
  "model_score": 0.5583,
  "style_score": 0.4915,
  "label": "We cannot confidently determine whether this text was written by a human or AI.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "9a251edf-fbc9-422e-b90a-3d890a025d68",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.55,
  "model_score": 0.0,
  "style_score": 0.45,
  "label": "This writing shows patterns associated with human-written text.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "db585a99-e321-462a-a2ce-ed616ba5c0d2",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.4888,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "This writing shows patterns associated with human-written text.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "058bf625-f49c-4d09-9d40-e02c8ead1c73",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.4476,
  "model_score": 0.9976,
  "style_score": 0.45,
  "label": "This writing shows patterns associated with AI-generated text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "28d2febe-b049-4322-87c4-79e188e51270",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.4969,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "This writing shows patterns associated with AI-generated text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "ca92315a-2a95-4984-b77b-3e9b10e4cff4",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.4064,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "This writing shows patterns associated with AI-generated text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "c0802276-c184-4317-a0eb-ad7f08a0f833",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.6986,
  "model_score": 0.9876,
  "style_score": 0.711,
  "label": "This writing shows patterns associated with AI-generated text, but the result is not definitive.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "26f40403-dcad-4954-87e9-55470032396e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5213,
  "model_score": 0.0287,
  "style_score": 0.45,
  "label": "This writing shows patterns associated with human-written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "3eb9c09b-5fed-438b-b5a5-836e1cc05d5e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5213,
  "model_score": 0.0287,
  "style_score": 0.45,
  "label": "This writing shows patterns associated with human-written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "7c7549d0-db85-49c5-b3cb-05e9c414026b",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5213,
  "model_score": 0.0287,
  "style_score": 0.45,
  "label": "This writing shows patterns associated with human-written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "2499ca6a-9f3a-40cc-9b6b-75840625c370",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5213,
  "model_score": 0.0287,
  "style_score": 0.45,
  "label": "This writing shows patterns associated with human-written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "fb668e1f-04a8-4068-8662-b385d89b8922",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5213,
  "model_score": 0.0287,
  "style_score": 0.45,
  "label": "This writing shows patterns associated with human-written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "2a5751a3-25ce-4c19-9b37-905cc1070cf5",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5213,
  "model_score": 0.0287,
  "style_score": 0.45,
  "label": "This writing shows patterns associated with human-written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "1cc89afc-9225-4285-9c94-35640c10d28c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5213,
  "model_score": 0.0287,
  "style_score": 0.45,
  "label": "This writing shows patterns associated with human-written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "3f2253eb-508d-48bd-a963-0f03adcd4198",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5213,
  "model_score": 0.0287,
  "style_score": 0.45,
  "label": "This writing shows patterns associated with human-written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "beda4f26-ba24-4a12-b08d-eb5102e15524",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5213,
  "model_score": 0.0287,
  "style_score": 0.45,
  "label": "This writing shows patterns associated with human-written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "869a5761-3e3c-4e6e-a003-36935d2818fb",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5213,
  "model_score": 0.0287,
  "style_score": 0.45,
  "label": "This writing shows patterns associated with human-written text.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
