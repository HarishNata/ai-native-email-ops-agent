from app.models import FollowUpTask, Intent, Priority


def create_follow_up_task(intent: Intent, priority: Priority) -> FollowUpTask | None:
    if intent == "project_request":
        return FollowUpTask(
            title="Prepare and send GitHub project repo",
            reason="Contact requested a project example with a GitHub link",
            due_hint="Within 24 hours",
        )

    if intent == "scheduling":
        return FollowUpTask(
            title="Confirm meeting availability",
            reason="Message includes scheduling intent",
            due_hint="Same day if possible",
        )

    if priority == "high":
        return FollowUpTask(
            title="Respond to high-priority message",
            reason="Message was scored as high priority",
            due_hint="Today",
        )

    return None
