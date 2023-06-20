import pytest
from dotenv import load_dotenv
from starlette.testclient import TestClient
from app.main import app


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as client:
        yield client
