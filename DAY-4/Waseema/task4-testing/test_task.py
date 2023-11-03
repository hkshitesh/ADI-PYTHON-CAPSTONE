from app_task import app
import pytest

@pytest.fixture()
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_valid_register(client):
    response = client.post('/register',data=dict(username='wasee',email='sellsathath@gmail.com',password='123'), follow_redirects = True)
    data = response.data.decode()
    assert data == "Registration successful for wasee"