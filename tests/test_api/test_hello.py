from app.main import app
from tests.client import TestClient

PREFIX = "/hello"
client = TestClient(PREFIX, app)


class TestHello:
    def test_get(self):
        response = client.get("/get")
        assert response.text.lower() == "hello!"
