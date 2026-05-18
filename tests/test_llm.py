from app.agent import EmailOpsAgent
from app.models import LLMWorkflowAnalysis


def test_agent_uses_llm_when_available(monkeypatch):
    monkeypatch.setattr("app.services.llm.is_available", lambda: True)

    def fake_analyze(message: str) -> LLMWorkflowAnalysis:
        return LLMWorkflowAnalysis(
            intent="project_request",
            priority="high",
            action_items=["Share sanitized GitHub portfolio repo"],
            draft_reply="Hi,\n\nHappy to share a public demo repo.\n\nBest,\nHarish",
        )

    monkeypatch.setattr("app.services.llm.analyze_message", fake_analyze)

    result = EmailOpsAgent().run("Can you send a GitHub repo?")
    assert result.processing_mode == "llm"
    assert result.intent == "project_request"
    assert result.priority == "high"
    assert len(result.action_items) >= 1


def test_agent_falls_back_to_rules_when_llm_fails(monkeypatch):
    monkeypatch.setattr("app.services.llm.is_available", lambda: True)

    def failing_analyze(message: str) -> LLMWorkflowAnalysis:
        raise RuntimeError("OpenAI unavailable")

    monkeypatch.setattr("app.services.llm.analyze_message", failing_analyze)

    result = EmailOpsAgent().run("Do you have a GitHub repo of a project?")
    assert result.processing_mode == "rules"
    assert result.intent == "project_request"
