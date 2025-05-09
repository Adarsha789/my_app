from src.app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to My Flask App!" in response.data
    assert b"Enter your name:" in response.data
