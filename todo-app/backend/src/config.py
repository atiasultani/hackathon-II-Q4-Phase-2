from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    BETTER_AUTH_SECRET: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 43200
    APP_NAME: str = "Todo API"
    DEBUG: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
