# Acceptance Criteria — Provenance Guard

These five acceptance criteria describe how I will evaluate whether Provenance Guard works as expected. Each criterion includes a measurable target and an explanation of why it matters.

These targets were documented after the initial implementation and will be used to evaluate the system in future testing.

---

## 1. False Positive Rate

**Target:** When testing 10 human-written samples, no more than 1 should be incorrectly labeled as high-confidence AI. This target should hold in each of three testing trials.

**Why this target:**

False positives can unfairly accuse someone of using AI when they wrote the content themselves. I want the system to be careful about making these decisions because protecting genuine writers is more important than detecting every AI-generated submission.

---

## 2. Score Separation

**Target:** When testing 10 human-written samples and 10 AI-generated samples, the average combined score for AI-generated text should be at least 0.15 higher than the average score for human-written text in each of three trials.

**Why this target:**

The system uses two different signals to analyze writing. I chose this target because I want the combined scores to show a noticeable difference between the two categories. A measurable gap will help determine whether combining the signals actually improves the results.

---

## 3. Label Coverage

**Target:** All three labels—high-confidence human, unsure, and high-confidence AI—must be reachable. Testing scores of 0.20, 0.50, and 0.90 should return human, unsure, and AI, respectively. Every score between 0 and 1 must map to exactly one label.

**Why this target:**

The system should not force every submission into either human or AI. Some writing is difficult to classify, so having an unsure option is important. I want all three labels to work correctly and communicate the results clearly to users.

---

## 4. Appeal Handling

**Target:** All 5 out of 5 valid appeals must be recorded in the audit log and change the submission's status to `under_review`. An appeal using an unknown content ID must return HTTP 404.

**Why this target:**

AI detection is not always accurate, and writers should have a way to challenge a decision. Every valid appeal should be recorded so the writer's concern is not lost. I chose a 100% target because recording an appeal is a basic requirement of the service.

---

## 5. Invalid Input Handling

**Target:** All 5 out of 5 invalid requests must return HTTP 400 instead of crashing the service. The test cases will include missing text, empty text, whitespace-only text, missing creator ID, and JSON that is not an object.

**Why this target:**

Users may accidentally submit incomplete or invalid information. The service should handle these requests without crashing or producing misleading results. I want the endpoint to return clear errors so users understand what needs to be corrected.

---

## Conclusion

These five criteria focus on reducing false accusations, measuring score differences, providing meaningful labels, handling appeals, and validating user input.

The goal is not to create a perfect AI detector, but to build a system that is measurable, transparent, and fair to writers. Any targets the system fails to meet during future testing should be documented and investigated rather than silently changed.

---

## Capstone

Written before any capstone results, for the Shape B extension (failure handling on the scoring stage of `/submit`).

The exact test inputs for criteria 1, 3 and 4 (the 10 invalid texts, the 10 short sentences from my own essay, and the two broken-server setups) are fixed in `capstone_eval.py` and `run_without_torch.py`, committed with these criteria.

### 1. Refusing Invalid Text

**Target:** When 10 invalid text submissions are tested, including single characters, punctuation-only text, emojis, and random keyboard characters, the system must reject all 10 out of 10 requests with HTTP 400 and a clear JSON error message instead of generating an AI or human classification.

**Why:** Text without meaningful content cannot be evaluated reliably. I chose 10 out of 10 because even one incorrect classification could mislead users or unfairly label their writing.

### 2. Recording Failed Requests in the Audit Log

**Target:** For 10 intentionally refused or failed requests, all 10 must produce an entry in `logs/audit.jsonl`. Each entry must contain the original `creator_id` and a status indicating that the request was refused or failed.

**Why:** Every failed request should be traceable so I can identify problems and investigate errors. I chose 100% because missing even one failure could make debugging difficult and leave an incomplete record of what happened.

### 3. Accepting Valid Short Human Writing

**Target:** Out of 10 meaningful human-written samples containing 8–20 words each, at least 9 out of 10 must be accepted and scored rather than refused. An accepted response must include a confidence score and a label.

**Why:** Short writing is not necessarily invalid. I chose 9 out of 10 because refusing too many legitimate submissions would make the system unreliable for real writers. Allowing one rejection accounts for borderline cases while still maintaining a high acceptance rate.

### 4. Handling Missing Model Dependencies

**Target:** In 2 out of 2 simulated failure scenarios, one with PyTorch unavailable and one with GPT-2 unavailable, the system must return HTTP 503 with a JSON error explaining that scoring is unavailable, without producing a false classification or an unhandled server error.

**Why:** The system depends on external model components that might not always be available. I chose 2 out of 2 because both known dependency failures should be handled safely rather than causing the service to crash or return unreliable results.

### 5. Recording Performance and Text Information

**Target:** Across 20 submissions, including 10 accepted and 10 refused requests, all 20 corresponding audit records must include `duration_ms` as a nonnegative number and `text_chars` as an integer matching the submitted text's character count.

**Why:** These fields help me understand how long requests take and what types of submissions cause problems. I chose 20 out of 20 because complete records are necessary for comparing successful and failed requests accurately.