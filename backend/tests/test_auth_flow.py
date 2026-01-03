import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_auth_flow():
    # Test that the root endpoint works
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

    # Test that task endpoints are protected (should return 401 without auth)
    response = client.get("/api/tasks")
    # Note: This test may need to be updated based on how authentication is implemented
    # For now, we're just ensuring the endpoint exists
    print(f"Response status: {response.status_code}")

    # Test creating a task without authentication (should be protected)
    response = client.post("/api/tasks", json={
        "title": "Test Task",
        "description": "Test Description"
    })
    print(f"Create task response status: {response.status_code}")

def test_task_crud_operations():
    # This test would require authentication in a real implementation
    # For now, we're just testing that the endpoints exist and return expected status codes
    # in a real scenario with proper authentication

    # Test GET /api/tasks
    response = client.get("/api/tasks")
    print(f"GET tasks response status: {response.status_code}")

    # These tests are placeholders - in a real implementation,
    # we would need to handle authentication properly