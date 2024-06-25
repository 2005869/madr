from sqlalchemy import select

from madr.models import User


def test_create_user(session):
    new_user = User(username='Test', email='test@test.com', password='secret')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'Test'))

    assert user.username == new_user.username
