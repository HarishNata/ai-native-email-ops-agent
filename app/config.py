from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_env: str = Field(default="demo")
    database_path: Path = Field(default=Path("agent_memory.db"))
    log_dir: Path = Field(default=Path("logs"))
    openai_api_key: str | None = Field(default=None)
    openai_model: str = Field(default="gpt-4o-mini")
    use_llm: bool = Field(default=True)

    @property
    def llm_enabled(self) -> bool:
        return self.use_llm and bool(self.openai_api_key)


settings = Settings()
