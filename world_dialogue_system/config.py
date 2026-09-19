"""Application configuration.

Loads settings from environment variables / a `.env` file using
`pydantic-settings`. All configuration is strongly typed and validated at
startup, so missing or malformed values fail fast rather than silently.
"""

from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Typed application settings loaded from the environment."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    app_name: str = "WorldDialogueSystem"
    app_env: Literal["development", "staging", "production"] = "development"
    log_level: str = "INFO"
    debug: bool = False


@lru_cache
def get_settings() -> Settings:
    """Return a cached, singleton `Settings` instance."""
    return Settings()


settings = get_settings()
