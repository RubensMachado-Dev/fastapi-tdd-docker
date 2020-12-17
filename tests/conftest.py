# project/tests/conftest.py


import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from app.db import generate_schema, get_db
from app.main import create_application  # updated
from app.config import get_settings, Settings
from app.models.sqlalchemy_model import Base


def get_settings_override() -> Settings:
    return Settings(testing=1)


@pytest.fixture(scope="module")
def test_app():
    app = create_application()  # new
    app.dependency_overrides[get_settings] = get_settings_override

    generate_schema()
    with TestClient(app) as test_client:  # updated

        # testing
        yield test_client

    # tear down


@pytest.fixture(scope="module")
def test_app_with_db():
    def override_get_db():
        try:
            db = testing_session_local()
            yield db
        finally:
            db.close()

    if os.environ.get("DATABASE_TEST_URL"):
        SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_TEST_URL")
    else:
        SQLALCHEMY_DATABASE_URL = "postgres://postgres:postgres@localhost:5432/web_test"

    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    testing_session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    app = create_application()  # new
    app.dependency_overrides[get_settings] = get_settings_override
    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:  # updated

        # testing
        yield test_client

    # tear down
