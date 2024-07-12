from http import HTTPStatus

from fastapi.testclient import TestClient

from madr.app import app


def test_index_return_message():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'index page'}
