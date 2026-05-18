from datetime import datetime, timezone
from typing import Literal
from pydantic import BaseModel, Field


Intent = Literal[
    "project_request",
    "scheduling",
    "job_opportunity",
    "follow_up",
    "thank_you",
    "general"
]

Priority = Literal["low", "medium", "high"]

ProcessingMode = Literal["llm", "rules"]


class AgentRequest(BaseModel):
    message: str = Field(min_length=1)


class FollowUpTask(BaseModel):
    title: str
    reason: str
    due_hint: str | None = None
    completed: bool = False


class LLMWorkflowAnalysis(BaseModel):
    intent: Intent
    priority: Priority
    action_items: list[str] = Field(min_length=1, max_length=5)
    draft_reply: str = Field(min_length=1)


class AgentResult(BaseModel):
    message: str
    intent: Intent
    priority: Priority
    action_items: list[str]
    needs_follow_up: bool
    follow_up_task: FollowUpTask | None = None
    draft_reply: str
    processing_mode: ProcessingMode = "rules"
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
