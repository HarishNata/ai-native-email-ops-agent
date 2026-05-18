from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_agent_run_endpoint():
    response = client.post(
        "/agent/run",
        json={"message": "Do you have a GitHub repo of a project?"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["intent"] == "project_request"
    assert data["priority"] == "high"
    assert data["needs_follow_up"] is True
    assert len(data["action_items"]) >= 1
