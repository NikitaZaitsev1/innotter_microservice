import os

from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    DB_URL: str = os.getenv("DB_URL")
    DEBUG: int = os.getenv("DEBUG")
    AMQP_URL: str = os.getenv("AMQP_URL")
    AWS_ACCESS_KEY_ID: str = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: str = os.getenv("AWS_SECRET_ACCESS_KEY")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")

    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()
