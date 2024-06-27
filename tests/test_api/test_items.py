from app.main import app
from tests.client import TestClient

PREFIX = "/items"
client = TestClient(PREFIX, app)


class TestItem:
    def test_get(self):
        response = client.get("/items")
        # TODO
