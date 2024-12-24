import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def test_user_data():
    return { "name": "User", "email": "user@example.com", "password": "123456" }

def test_create_user(test_user_data):
    client.delete("/api/v1/users/99999")

    response = client.post("/api/v1/users/", json=test_user_data)

    print(response.json())
    assert response.status_code == 200
    assert response.json()["name"] == test_user_data["name"]


def test_get_user_not_found():
    response = client.get("/api/v1/users/99999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}
