from http import HTTPStatus

user_model = {
    'firstname': 'Bob',
    'username': 'bobmarley',
    'email': 'bob@marley.com',
    'password': 'secret',
}

user_model_response = {
    'firstname': 'Bob',
    'username': 'bobmarley',
    'email': 'bob@marley.com',
    'id': 1,
}

user_update_model = {
    'firstname': 'Santos',
    'username': 'santosdummont',
    'email': 'santos@dummont.com',
    'password': 'secret',
}

user_update_model_response = {
    'firstname': 'Santos',
    'username': 'santosdummont',
    'email': 'santos@dummont.com',
    'id': 1,
}


def test_index_return_message(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'index page'}


def test_create_user(client):
    response = client.post('/users', json=user_model)

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == user_model_response


def test_list_users_in_db(client):
    response = client.get('/users')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == [user_model_response]


def test_get_an_user_with_id(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_model_response


def test_update_an_user(client):
    response = client.put('/users/1', json=user_update_model)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == user_update_model_response


def test_update_an_user_with_invalid_id(client):
    response = client.put('/users/1000', json=user_update_model)

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Invalid id'}


def test_delete_an_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted with success'}


def test_delete_an_user_with_invalid_id(client):
    response = client.delete('/users/1000')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Invalid id'}
