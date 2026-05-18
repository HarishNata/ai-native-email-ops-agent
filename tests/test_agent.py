from app.agent import EmailOpsAgent


def test_agent_project_request():
    agent = EmailOpsAgent()
    result = agent.run("Do you have a GitHub repo of a project?")
    assert result.intent == "project_request"
    assert result.priority == "high"
    assert result.needs_follow_up is True
    assert "GitHub" in result.draft_reply
