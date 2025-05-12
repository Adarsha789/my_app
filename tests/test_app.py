from src.app import app

# Disable CSRF during testing
app.config["WTF_CSRF_ENABLED"] = False
app.config["TESTING"] = True


def test_home_page_loads():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Enter your name:" in response.data


def test_form_submission():
    client = app.test_client()
    response = client.post("/", data={"name": "Adarsha"}, follow_redirects=False)
    assert response.status_code == 302
    assert response.location.endswith("/success")
