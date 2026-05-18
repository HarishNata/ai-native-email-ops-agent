import sqlite3
from app.config import settings
from app.models import AgentResult


class AgentStorage:
    def __init__(self):
        self.db_path = settings.database_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS agent_runs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message TEXT NOT NULL,
                intent TEXT NOT NULL,
                priority TEXT NOT NULL,
                needs_follow_up INTEGER NOT NULL,
                draft_reply TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            '''
        )
        conn.commit()
        conn.close()

    def save_result(self, result: AgentResult) -> None:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            '''
            INSERT INTO agent_runs
            (message, intent, priority, needs_follow_up, draft_reply, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
            ''',
            (
                result.message,
                result.intent,
                result.priority,
                int(result.needs_follow_up),
                result.draft_reply,
                result.created_at.isoformat(),
            ),
        )
        conn.commit()
        conn.close()
