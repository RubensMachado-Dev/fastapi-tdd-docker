import logging

from sqlalchemy import create_engine


from sqlalchemy.orm import sessionmaker

from models.sqlalchemy_model import Base

log = logging.getLogger(__name__)  # new

engine = create_engine("postgres://postgres:postgres@web-db:5432/web_dev")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db() -> None:
    pass


def generate_schema() -> None:
    # from app.config import Settings
    # settings=Settings()
    log.info("Initializing Sql Alchemy...")
    log.info("Generating database schema via SQLAlchemy...")
    Base.metadata.create_all(bind=engine)
    SessionLocal.close_all()


# new
if __name__ == '__main__':
    generate_schema()


