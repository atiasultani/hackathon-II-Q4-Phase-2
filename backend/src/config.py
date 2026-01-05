from pydantic import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """
    app_name: str = "Todo App API"
    database_url: str = "postgresql://username:password@localhost:5432/todo_app"
    secret_key: str = "your-super-secret-key-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 1440  # 24 hours
    debug: bool = False

    class Config:
        env_file = ".env"


# Create settings instance
settings = Settings()