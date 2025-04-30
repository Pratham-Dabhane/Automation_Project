import app
import pytest

def test_hello_route():
    client = app.app.test_client()
    response = client.get('/hello')
    assert response.status_code == 200
    assert b"Hello World!" in response