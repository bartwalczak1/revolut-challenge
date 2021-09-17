from pytest import fixture
from app import api


@fixture(scope="function")
def client():
    """
    Create a Flask test client.
    """
    app = api.run_app()
    app.testing = True
    yield app.test_client()
