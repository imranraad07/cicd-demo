from app import app

def test_home():
    tester = app.test_client()
    response = tester.get("/")

    assert response.status_code == 200
    assert response.data in b"Hello from Flask!"


def test_about():
    tester = app.test_client()
    response = tester.get("/about")

    assert response.status_code == 200
    assert response.data in b"This is a simple CI/CD Demo!"    


def test_name():
    tester = app.test_client()
    response = tester.get("/Alice")

    assert response.status_code == 200
    assert response.data in b"Hello, Alice!"        