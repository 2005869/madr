from http import HTTPStatus

usertest = {
    'username': 'bobmarley',
    'email': 'bob@marley.com',
    'senha': 'secret',
}

userresponse = {'username': 'bobmarley', 'email': 'bob@marley.com', 'id': 1}
detail_user_not_found = {'detail': 'User not found'}


def test_get_a_user(client, user):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == userresponse


def test_get_an_invalid_id(client, user):
    response = client.get('/users/5')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == detail_user_not_found
