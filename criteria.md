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