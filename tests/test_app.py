from http import HTTPStatus


def test_index_receive_message(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'home do projeto'}
