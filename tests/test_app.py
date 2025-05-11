from src.app import app


def test_home():
    """Test the home page (GET request)."""
    client = app.test_client()
    response = client.get("/")

    # Test status code and content
    assert response.status_code == 200
    assert b"Enter your name:" in response.data
    assert b"Submit" in response.data


def test_form_submission():
    """Test form submission (POST request)."""
    client = app.test_client()

    # Submit a form with a name
    response = client.post("/", data={"name": "Adarsha"})

    # Test status code and content after form submission
    assert response.status_code == 302
    assert b"Hello, Adarsha!" in response.data

    # Test if the data was successfully added (check for name)
    response = client.get("/")
    assert b"Adarsha" in response.data
