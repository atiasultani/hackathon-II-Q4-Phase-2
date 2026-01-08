from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    # Database settings
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    NEON_DATABASE_URL: str = os.getenv("NEON_DATABASE_URL", "")

    # Auth settings
    BETTER_AUTH_SECRET: str = os.getenv("BETTER_AUTH_SECRET", "your-super-secret-jwt-key-here-make-it-long-and-random")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "43200"))  # 30 days

    # Application settings
    APP_NAME: str = "Todo API"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    class Config:
        env_file = ".env"

settings = Settings()