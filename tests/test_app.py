from http import HTTPStatus


def test_index_recebe_mensagem(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'home do projeto'}
