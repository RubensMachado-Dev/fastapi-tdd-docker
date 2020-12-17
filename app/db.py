import logging
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings
from app.models.sqlalchemy_model import Base

log = logging.getLogger(__name__)  # new

SQLALCHEMY_DATABASE_URL = settings.database_url
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    """
    Returns connection session of database
     """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def generate_schema() -> None:
    log.info("Initializing Sql Alchemy...")
    log.info("Generating database schema via SQLAlchemy...")
    engine = create_engine(settings.database_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)


# new
if __name__ == '__main__':
    generate_schema()
