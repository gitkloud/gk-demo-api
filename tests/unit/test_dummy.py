# Endpoint returns a JSON response
import fastapi

def test_endpoint_returns_json_response(self):
    from fastapi.testclient import TestClient
    from src.main import app

    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello"}

# Endpoint returns a 200 status code
def test_auth_endpoint_returns_200(self):
    from fastapi.testclient import TestClient
    from src.main import app

    client = TestClient(app)
    response = client.get("/v1/oauth")
    assert response.status_code == 200
