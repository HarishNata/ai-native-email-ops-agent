from app.models import Intent


def draft_reply(message: str, intent: Intent) -> str:
    if intent == "project_request":
        return (
            "Hi,\n\n"
            "Thanks for reaching out. I can share a cleaned demo version of one of my AI projects. "
            "The original production work includes client-specific details, so I am preparing a sanitized GitHub repo "
            "that still demonstrates the core automation, agent workflow, and engineering approach.\n\n"
            "Best,\nHarish"
        )

    if intent == "scheduling":
        return (
            "Hi,\n\n"
            "Thanks for reaching out. I would be happy to schedule a time to connect. "
            "I am available later this week and can work around your schedule.\n\n"
            "Best,\nHarish"
        )

    if intent == "job_opportunity":
        return (
            "Hi,\n\n"
            "Thank you for reaching out. I would be excited to learn more about the role. "
            "My experience includes AI automation, agentic workflows, QA testing, API integrations, and Python-based backend development.\n\n"
            "Best,\nHarish"
        )

    if intent == "follow_up":
        return (
            "Hi,\n\n"
            "Thanks for following up. I appreciate the reminder and will send an update shortly.\n\n"
            "Best,\nHarish"
        )

    if intent == "thank_you":
        return (
            "Hi,\n\n"
            "Thank you, I really appreciate it. I look forward to staying connected.\n\n"
            "Best,\nHarish"
        )

    return (
        "Hi,\n\n"
        "Thanks for your message. I appreciate you reaching out and would be happy to follow up.\n\n"
        "Best,\nHarish"
    )
