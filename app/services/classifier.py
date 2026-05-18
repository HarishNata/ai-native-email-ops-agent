from app.models import Intent


def classify_message(message: str) -> Intent:
    text = message.lower()

    if any(word in text for word in ["checking in", "follow up", "following up"]):
        return "follow_up"

    if any(word in text for word in ["github", "repo", "portfolio", "project", "link"]):
        return "project_request"

    if any(word in text for word in ["schedule", "meeting", "call", "available", "calendar"]):
        return "scheduling"

    if any(word in text for word in ["job", "role", "opening", "hiring", "internship"]):
        return "job_opportunity"

    if any(word in text for word in ["thank", "appreciate", "grateful"]):
        return "thank_you"

    return "general"
