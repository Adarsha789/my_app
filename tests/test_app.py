from src.app import app


def test_home_page_loads():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Enter your name:" in response.data


def test_form_submission():
    """Test if submitting a form redirects to the success page"""

    client = app.test_client()

    response = client.post("/", data={"name": "Adarsha"}, follow_redirects=False)

    assert response.status_code == 302

    location = response.location
    assert location.endswith("/success")
