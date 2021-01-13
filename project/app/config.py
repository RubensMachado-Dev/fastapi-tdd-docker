# project/app/config.py
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
import logging
from functools import lru_cache

from pydantic import BaseSettings

log = logging.getLogger(__name__)


class Settings(BaseSettings):
    environment: str
    testing: bool
    database_url: str

    class Config:
        env_file = "../../.env"
        # env_file_encoding = 'utf-8'
        # keep_untouched = (cached_property,)


#@lru_cache(maxsize=1)
def get_settings() -> BaseSettings:
    log.warning("Loading config settings from the environment...")
    return Settings()


settings = get_settings()
