import json
from datetime import datetime, timezone
from pathlib import Path
from app.config import settings


def log_run(payload: dict) -> None:
    settings.log_dir.mkdir(parents=True, exist_ok=True)
    log_path = settings.log_dir / "agent_runs.jsonl"

    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        **payload,
    }

    with open(log_path, "a", encoding="utf-8") as file:
        file.write(json.dumps(entry) + "\n")
