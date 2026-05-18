from app.models import Intent


def extract_action_items(message: str, intent: Intent) -> list[str]:
    if intent == "project_request":
        return ["Send a cleaned GitHub repo or demo project"]

    if intent == "scheduling":
        return ["Provide availability", "Confirm meeting time"]

    if intent == "job_opportunity":
        return ["Reply with interest", "Share resume or portfolio if requested"]

    if intent == "follow_up":
        return ["Respond with a clear status update"]

    if intent == "thank_you":
        return ["Acknowledge the message politely"]

    return ["Review message and respond appropriately"]
