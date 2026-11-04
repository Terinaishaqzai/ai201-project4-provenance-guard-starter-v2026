# Provenance Guard

Provenance Guard is a Python backend service that analyzes submitted writing and estimates whether it shows patterns associated with human-written or AI-generated text. It combines two different detection signals, produces a confidence score and a readable label, and allows writers to appeal a decision.

The service is built using Python and Flask. All detection runs locally without requiring an external API key.

For setup and execution instructions, see [RUNNING.md](RUNNING.md).

---

## What This Does

Provenance Guard processes submitted text through the following steps:

1. **Receive a submission:** The user sends a POST request to `/submit` containing `text` and `creator_id`.

2. **Validate the input:** The system checks that the required fields exist and contain valid information. Invalid submissions return an error instead of being processed.

3. **Generate a content ID:** Each valid submission receives a unique `content_id` using Python's UUID library.

4. **Analyze the writing:** The system runs two different signals. The model signal analyzes how predictable the text is, while the style signal measures sentence length variation, vocabulary diversity, and punctuation.

5. **Calculate the combined score:** Both signal scores are combined using a weighted average. The result is between 0 and 1, where higher scores indicate more AI-like patterns.

6. **Assign a label:** The combined score is compared against configured thresholds to assign one of three labels: high-confidence human, unsure, or high-confidence AI.

7. **Record and return the result:** The system saves the decision in `logs/audit.jsonl` and returns structured JSON containing the content ID, guess, confidence, label, and both signal scores.

Writers can also submit an appeal through POST `/appeal` by providing a valid `content_id` and their reasoning. The system records the appeal, changes the submission's current status to `under_review`, and returns a confirmation.

The original decision remains in the audit log so the history can be reviewed later.

---

## Signals and Scoring

### Signal One — The Model Signal

**What it measures:**

The first signal is implemented in `detector.py` using a locally running GPT-2 language model. It measures how predictable the submitted text is to the model.

The function `detector.model_signal(text)` returns a score between 0 and 1, where higher values indicate writing patterns that the model considers more predictable.

**Why that might differ between human and AI writing:**

AI-generated writing can contain predictable word sequences, consistent sentence structures, and repeated language patterns. A language model may find these patterns easier to predict.

Human writing can contain more unexpected wording, personal expressions, and unusual sentence structures.

**What it can't see:**

This signal cannot prove who wrote the text. A human can write predictable or formal sentences, and AI-generated text can be edited to appear less predictable.

It may incorrectly classify structured human writing or fail to recognize heavily edited AI-generated content.

The score also depends on how the language model processes the text, so it should not be treated as definitive evidence of authorship.

### Signal Two — The Style Signal

**What it measures:**

The second signal is implemented in `stylometry.py`. It analyzes the structure of the writing without trying to understand its meaning.

I implemented three measurements:

- **Sentence length spread:** Measures how much sentence lengths vary using the standard deviation divided by the average sentence length.
- **Type-token ratio:** Measures vocabulary diversity by dividing the number of unique words by the total number of words.
- **Punctuation density:** Measures selected punctuation marks relative to the number of words.

These measurements are normalized and combined into a score between 0 and 1.

The style signal uses the following internal weights:

| Measurement | Weight |
|---|---|
| Sentence length spread | 0.50 |
| Vocabulary diversity | 0.30 |
| Punctuation density | 0.20 |

**Why that might differ between human and AI writing:**

AI-generated writing can have more consistent sentence lengths and repeated patterns.

Human writing may include greater variation in sentence length, vocabulary, and punctuation.

Measuring these characteristics gives the system another perspective beyond the language model's prediction.

**What it can't see:**

The style signal does not understand the meaning or context of the text.

A human might naturally write consistent sentences, while someone could change AI-generated text by adding unusual punctuation, changing sentence lengths, or introducing typos.

Vocabulary diversity also depends on text length, so scores from very short and long submissions may not be directly comparable.

These weaknesses mean the style signal is only a heuristic, not a reliable standalone detector.

### The Combining Rule

**The rule:**

I use a weighted average to combine both signals.

Both signals return values between 0 and 1, with higher values indicating more AI-like writing patterns.

I chose equal weights so that neither signal completely determines the result.

**The numbers:**

```python
WEIGHT_MODEL_SIGNAL = 0.5
WEIGHT_STYLE_SIGNAL = 0.5
```

The combining formula is:

```python
combined_score = (
    0.5 * model_score
    + 0.5 * style_score
)
```

The final score is used to determine the label.

When the two signals strongly disagree, their average can move toward the middle of the scoring range. This makes an unsure result more likely instead of automatically trusting one signal.

**Where it lives:** `scoring.py::combine_signals`

The weights are configured in `config.py`.

**A case where my two signals split, and what my rule does with it:**

I tested the following text:

> I love programming. Sometimes it is challenging, but I enjoy solving problems! Learning something new every day makes it exciting.

The results were:

| Signal | Score |
|---|---|
| Model signal | 0.6397 |
| Style signal | 0.3286 |
| Combined score | 0.48415 |

The model signal gave a relatively high AI-likelihood score, but the style signal gave a lower score.

Using equal weights:

```python
combined_score = (0.6397 * 0.5) + (0.3286 * 0.5)
combined_score = 0.48415
```

The combined score falls into the unsure category.

This example shows why combining signals can be useful. When different methods disagree, the system does not need to make a strong accusation.

In another test, the model score was `0.4029` and the style score was `0.6618`, producing a combined score of `0.53235`, which also falls into the unsure range.

Neither result establishes the actual author of the sample.

**Confidence calculation:**

The application also calculates a confidence value using:

```python
confidence = round(2 * abs(combined_score - 0.5), 4)
```

This measures distance from the midpoint. It is a heuristic certainty indicator, not a statistically calibrated probability that the guess is correct.

---

## Label Variants

The system uses three labels based on the combined score.

The thresholds are defined in `config.py`:

```python
HUMAN_THRESHOLD = 0.35
AI_THRESHOLD = 0.65
```

| Label | Score range | Exact text a reader sees |
|---|---|---|
| High-confidence human | 0.00 ≤ score ≤ 0.35 | This writing shows patterns associated with human-written text. |
| Unsure | 0.35 < score < 0.65 | We cannot confidently determine whether this text was written by a human or AI. |
| High-confidence AI | 0.65 ≤ score ≤ 1.00 | This writing shows patterns associated with AI-generated text, but the result is not definitive. |

**Why I worded the unsure one this way:**

I wanted the unsure label to communicate uncertainty without accusing the writer of cheating.

AI detection is not always accurate, and a person may have written every word themselves even when the system cannot classify the text confidently.

The label makes it clear that the system does not have enough evidence to make a strong decision.

I also avoided claiming certainty in the AI label because the result is based on patterns rather than verified authorship.

**Label testing:**

I tested `scoring.score_to_label()` with three values:

```python
scoring.score_to_label(0.2)
scoring.score_to_label(0.5)
scoring.score_to_label(0.9)
```

The results were:

```text
('human', 'This writing shows patterns associated with human-written text.')

('unsure', 'We cannot confidently determine whether this text was written by a human or AI.')

('ai', 'This writing shows patterns associated with AI-generated text, but the result is not definitive.')
```

All three labels are reachable through the label-mapping function.

---

## Sample Run

### A Submission

I submitted a sample through the `/submit` endpoint.

**Request:**

```bash
curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text":"The system provides efficient results. It processes information accurately. It generates consistent responses. It improves overall performance.","creator_id":"user123"}'
```

**Actual response:**

```json
{
  "combined_score": 0.53235,
  "confidence": 0.0647,
  "content_id": "a45b2478-6cce-4598-8c2f-9c17360de452",
  "guess": "unsure",
  "label": "We cannot confidently determine whether this text was written by a human or AI.",
  "model_score": 0.4029,
  "style_score": 0.6618
}
```

The request returned HTTP 200 OK.

The service generated a unique content ID, calculated both signal scores, combined them, and returned an unsure label.

### An Appeal

I tested the `/appeal` endpoint using the same content ID from the submission.

**Request:**

```bash
curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id":"a45b2478-6cce-4598-8c2f-9c17360de452","reasoning":"I wrote this text myself and would like the decision reviewed."}'
```

**Actual response:**

```json
{
  "content_id": "a45b2478-6cce-4598-8c2f-9c17360de452",
  "message": "Your appeal has been recorded.",
  "status": "under_review"
}
```

The appeal was accepted, and the submission's current status changed to `under_review`.

No automatic reclassification was performed.

### What the Log Shows Afterwards

**Request:**

```bash
curl "http://127.0.0.1:5000/log?limit=2"
```

**Actual response:**

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.53235,
      "content_id": "a45b2478-6cce-4598-8c2f-9c17360de452",
      "creator_id": "user123",
      "guess": "unsure",
      "label": "We cannot confidently determine whether this text was written by a human or AI.",
      "model_score": 0.4029,
      "status": "decided",
      "style_score": 0.6618,
      "timestamp": "2026-11-04T02:59:27+00:00"
    },
    {
      "content_id": "a45b2478-6cce-4598-8c2f-9c17360de452",
      "creator_id": "user123",
      "event": "appeal",
      "reasoning": "I wrote this text myself and would like the decision reviewed.",
      "status": "under_review",
      "timestamp": "2026-11-04T03:01:46+00:00"
    }
  ]
}
```

The audit log contains both the original decision and the appeal as separate entries.

The original entry remains unchanged, while the new appeal entry records the updated status.

This preserves the history of the submission and allows the system to track what happened.

---

## How I Used AI

### Moment 1 — Implementing the Style Signal

**What I asked for:**

I asked ChatGPT for step-by-step help implementing the functions in `stylometry.py`, including sentence length spread, type-token ratio, punctuation density, and the final style score.

**What came back:**

ChatGPT provided example Python implementations, explained how the measurements worked, and suggested a way to normalize and combine them into a score between 0 and 1.

**What I changed:**

I added the implementations to my project and tested the functions using different writing samples. I verified that the individual measurements returned numerical results and that the completed style signal produced different scores depending on the writing patterns.

### Moment 2 — Debugging the Submission Endpoint

**What I asked for:**

I asked ChatGPT to help identify why my updated `/submit` endpoint was not responding after I added the labeling and confidence calculations.

**What came back:**

ChatGPT reviewed my `app.py` code and identified syntax errors caused by extra commas in the `audit.log_decision()` function call.

It also helped me troubleshoot a missing Flask module caused by running the application outside the project's virtual environment.

**What I changed:**

I corrected the syntax errors, activated the project's virtual environment, and tested the endpoint again.

I confirmed that the endpoint returned the combined score, confidence, guess, label, and both signal scores correctly.

I also verified that the `/appeal` endpoint recorded an appeal and updated the status to `under_review`.

### Additional AI Assistance

I also used ChatGPT to help structure and draft project documentation and a proposed set of acceptance criteria. The criteria draft was created after the initial implementation and should not be represented as having been written before testing.

---

# Unit 8 — Testing and Improvement

The following sections are reserved for Unit 8. The attack experiments, evaluation trials, and improvements have not been completed yet. Results will be recorded here after the actual tests are performed.

---

## Rate Limiting

**Current configuration:**

```python
RATE_LIMITING_ENABLED = False
RATE_LIMIT_PER_MINUTE = 10
RATE_LIMIT_PER_DAY = 200
```

Rate limiting is currently disabled for Unit 7. These are the starter configuration values, not tested or finalized Unit 8 limits.

**Why those numbers and not others:**

To be determined during Unit 8.

**What a caller counts as:**

To be evaluated during Unit 8.

**The run of status codes when I pushed past it:**

Not tested yet.

---

## Attack Run — Before

Not completed yet.

The full attack set will be executed during Unit 8 using `run_attacks.py`.

**Ten audit log entries from the run:**

Pending actual attack results.

**The single worst outcome:**

To be identified after testing.

---

## Run Log and Verdicts

The five acceptance criteria will be evaluated across three trials during Unit 8 using `run_eval.py`.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. False positives | See criteria.md | Pending | Pending | Pending | Pending |
| 2. Score separation | See criteria.md | Pending | Pending | Pending | Pending |
| 3. Label coverage | See criteria.md | Pending | Pending | Pending | Pending |
| 4. Appeal handling | See criteria.md | Pending | Pending | Pending | Pending |
| 5. Invalid inputs | See criteria.md | Pending | Pending | Pending | Pending |

**Real output from one trial:**

Pending.

**Diagnoses:**

Any failed criteria or successful attacks will be analyzed to identify the affected stage and the reason for the failure.

---

## The Improvement

**What I changed:**

Pending Unit 8 testing.

**Which diagnosis pointed at it:**

Pending.

### Attack Run — After

Not completed yet.

**Did it help, and how do I know:**

To be determined by comparing the actual before-and-after results.

---

## What's Still Broken

To be completed after the Unit 8 attack set and evaluation.

**The trade I'd make if this ran for real:**

I would prioritize reducing false accusations against genuine writers, even if that meant some AI-generated submissions remained undetected. This would protect writers from unfair classifications, although the website would accept a higher risk of missing AI-generated content.

---

## Running the Project

See [RUNNING.md](RUNNING.md) for detailed setup instructions.

The project requires Python 3.13 according to its environment check. The existing Python 3.14 environment ran the tested endpoints but did not pass the version requirement.

Once a supported Python environment and the dependencies are installed, start the service:

```bash
python app.py
```

Run `curl` requests from a second terminal while the Flask server remains active.

The service runs locally at:

`http://127.0.0.1:5000`

---

## Repository

GitHub repository:

https://github.com/Terinaishaqzai/ai201-project4-provenance-guard-starter-v2026

This same repository will be used for Unit 8 so the project history and acceptance criteria remain available.