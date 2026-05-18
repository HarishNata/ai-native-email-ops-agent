from app.models import Intent, Priority


def score_priority(intent: Intent, message: str) -> Priority:
    text = message.lower()

    if intent in {"project_request", "job_opportunity"}:
        return "high"

    if any(word in text for word in ["tomorrow", "today", "urgent", "asap"]):
        return "high"

    if intent in {"scheduling", "follow_up"}:
        return "medium"

    return "low"
