from http import HTTPStatus

from fastapi import FastAPI

from madr.schemas import Message, User, UserPublic

app = FastAPI()


@app.get('/', response_model=Message)
def index_response():
    return {'message': 'home do projeto'}


@app.post('/contas', response_model=UserPublic, status_code=HTTPStatus.CREATED)
def register_user(user: User):
    return user
