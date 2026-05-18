import json
from pathlib import Path

from app.agent import EmailOpsAgent

SAMPLE_MESSAGES_PATH = Path(__file__).resolve().parents[1] / "data" / "sample_messages.json"


def test_sample_messages_match_expected_intents():
    samples = json.loads(SAMPLE_MESSAGES_PATH.read_text(encoding="utf-8"))
    agent = EmailOpsAgent()

    for sample in samples:
        result = agent.run(sample["message"])
        assert result.intent == sample["label"], (
            f"Expected {sample['label']} for message: {sample['message']!r}, "
            f"got {result.intent}"
        )
