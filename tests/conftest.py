import pytest
from flask import Flask, g
from flask.testing import FlaskClient
from httpx import Client
from sqlalchemy.orm import Session, sessionmaker

from app import middlewares, routes
from app.infrastructure import load_config
from app.infrastructure.database.session import create_session_maker

TEST_HOST = "http://test"


@pytest.fixture(scope="session")
def session_maker() -> sessionmaker:
    config = load_config()
    session_maker = create_session_maker(config.test_db_config.full_url)
    return session_maker


@pytest.fixture(scope="session")
def app(session_maker: sessionmaker) -> FlaskClient:
    app = Flask(__name__)

    middlewares.register(app, session_maker)
    routes.register(app)

    with app.test_client() as test_client:
        with app.app_context():
            yield test_client


class TestBaseClientClass:
    """Provides Test Class with loaded client fixture"""

    @pytest.fixture(autouse=True)
    def _a_provide_client(self, app: FlaskClient):
        """
            Provides a client for all tests in class.
            The "a" letter in the name required for loading these fixtures first, it"s not good but ok for now.
        """
        self.client = app


@pytest.fixture()
def _a_provide_session(app: FlaskClient, session_maker: sessionmaker):
    """
        Provides a client for all tests in class.
        The "a" letter in the name required for loading these fixtures first, it"s not good but ok for now.
    """
    g.session = session_maker()


class TestBaseClientDBClass(TestBaseClientClass):
    """Provides Test Class with loaded database and client fixture"""
