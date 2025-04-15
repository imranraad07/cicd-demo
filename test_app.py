from app import app

def test_home():
    tester = app.test_client()
    response = tester.get("/")

    assert response.status_code == 200
    assert response.data in b"Hello from Flask!"