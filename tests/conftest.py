import pytest


@pytest.fixture(autouse=True)
def isolated_runtime(tmp_path, monkeypatch):
    from app import config

    monkeypatch.setattr(config.settings, "database_path", tmp_path / "test.db")
    monkeypatch.setattr(config.settings, "log_dir", tmp_path / "logs")
    monkeypatch.setattr(config.settings, "use_llm", False)
    monkeypatch.setattr(config.settings, "openai_api_key", None)
