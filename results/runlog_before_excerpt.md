C1 trial 1 (first 3 of 10):
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.153,
    "model_score": 0.6086,
    "style_score": 0.5444,
    "label": "We cannot confidently determine whether this text was written by a human or AI.",
    "sent": "From the camel caravans of the medieval Silk Roads to the fiber optic "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.2051,
    "model_score": 0.475,
    "style_score": 0.3199,
    "label": "We cannot confidently determine whether this text was written by a human or AI.",
    "sent": "The earliest phase of globalization between 1000 and 1400 CE was built"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3366,
    "model_score": 0.4649,
    "style_score": 0.1985,
    "label": "This writing shows patterns associated with human-written text.",
    "sent": "By the seventeenth and eighteenth centuries, globalization expanded dr"
  }
]
C2 trial 1 (first 3 of 10):
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.3688,
    "model_score": 0.8061,
    "style_score": 0.5627,
    "label": "This writing shows patterns associated with AI-generated text, but the result is not definitive.",
    "sent": "Effective time management is an essential skill for students and profe"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.4681,
    "model_score": 0.9131,
    "style_score": 0.555,
    "label": "This writing shows patterns associated with AI-generated text, but the result is not definitive.",
    "sent": "Climate change represents one of the most pressing challenges facing o"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.4769,
    "model_score": 0.8868,
    "style_score": 0.5901,
    "label": "This writing shows patterns associated with AI-generated text, but the result is not definitive.",
    "sent": "Regular physical activity offers numerous benefits for both physical a"
  }
]
C3 trial 1:
{
  "spot_checks": {
    "0.2": "human",
    "0.5": "unsure",
    "0.9": "ai"
  },
  "spot_checks_passed": "3/3",
  "sweep_scores_checked": 1001,
  "sweep_failures": [],
  "sweep_passed": true,
  "pass": true
}
C4 trial 1:
{
  "valid_appeals_passed": "5/5",
  "unknown_id_status": 404,
  "unknown_id_response": {
    "error": "Content not found"
  },
  "first_appeal": {
    "submit_status": 200,
    "content_id": "b5b1fe3f-2998-45e1-be2b-6480ecb582fd",
    "appeal_status": 200,
    "appeal_response": {
      "content_id": "b5b1fe3f-2998-45e1-be2b-6480ecb582fd",
      "message": "Your appeal has been recorded.",
      "status": "under_review"
    },
    "logged_under_review": true,
    "pass": true
  }
}
C5 trial 1:
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing_text\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "     \n\t  "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": \"This request has text but no creator id at all, so it should be refused.\"}"
  }
]
{
  "case": "JSON body is a list, not an object",
  "status": 400,
  "response": {
    "error": "Invalid JSON object"
  },
  "pass": true
}
