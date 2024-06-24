from http import HTTPStatus

usertest = {
    'username': 'bobmarley',
    'email': 'bob@marley.com',
    'senha': 'secret',
}

userresponse = {
    'username': 'bobmarley',
    'email': 'bob@marley.com',
}


def test_index_recebe_mensagem(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'home do projeto'}


def test_register_user(client):
    response = client.post('/contas', json=usertest)
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == userresponse
