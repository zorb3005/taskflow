# tests/test_task.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks/", json={"title": "Test Task", "description": "Test task description"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"
