# project/app/config.py
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
import logging
# import os
from functools import lru_cache, cached_property

# from async_property import async_cached_property
# from databases import Database
from pydantic import BaseSettings, AnyUrl

log = logging.getLogger(__name__)


class Settings(BaseSettings):
    environment: str
    testing: bool
    database_url: AnyUrl

    class Config:
        env_file = "../../.env"
        # env_file_encoding = 'utf-8'
        # keep_untouched = (cached_property,)


# @lru_cache()
def get_settings() -> BaseSettings:
    log.warning("Loading config settings from the environment...")
    return Settings()


settings = Settings()
