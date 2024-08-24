# test_app.py

import pytest
from app import app

@pytest.fixture
def client():
    # Create a test client using the Flask app
    with app.test_client() as client:
        yield client

def test_add_numbers(client):
    # Send a GET request to the /add endpoint with query parameters a=5 and b=3
    response = client.get('/add?a=5&b=3')

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response JSON contains the correct sum
    assert response.json == {'sum': 8.0}
