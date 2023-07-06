import pytest
from proxy_server import app


def test_proxy_send_request():
    app.testing = True
    test_data = {"username": "value"}
    with app.test_client() as client:
        response = client.post("/proxy", json=test_data)
        assert response.status_code == 200
        assert response.json == {"message": "Sample Response"}


def test_status_request():
    app.testing = True
    with app.test_client() as client:
        response = client.get("/status")
        assert response.status_code == 200


if __name__ == "__main__":
    pytest.main()
