from app.services.classifier import classify_message


def test_project_request():
    assert classify_message("Can you send a GitHub repo?") == "project_request"


def test_scheduling():
    assert classify_message("Can we schedule a call?") == "scheduling"


def test_job_opportunity():
    assert classify_message("We have a job opening") == "job_opportunity"


def test_follow_up_overrides_project_keywords():
    message = "Just checking in to see if you had a chance to send the project link."
    assert classify_message(message) == "follow_up"
