
import logging
import os
from functools import lru_cache

from pydantic import BaseSettings


log = logging.getLogger(__name__)


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)


def get_settings() -> BaseSettings:
    log.warning("Loading config settings from the environment...")
    return Settings()