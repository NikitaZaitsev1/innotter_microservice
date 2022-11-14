import os

from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    DB_URL: str
    DEBUG: int
    AMQP_URL: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str

    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()
