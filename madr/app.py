from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from madr.schemas import Message, UserDB, UserPublic, UserSchema

app = FastAPI()


database = []


@app.get('/', response_model=Message)
def index():
    """Return a message for index page"""
    return {'message': 'index page'}


@app.post('/users', response_model=UserPublic, status_code=HTTPStatus.CREATED)
def create_user(user: UserSchema):
    """Register a user"""
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)

    return user_with_id


@app.get('/users', response_model=list[UserPublic])
def list_users():
    """List all users from database"""
    return database


@app.get('/users/{user_id}', response_model=UserPublic)
def return_an_user(user_id: int):
    """Get a user from id"""
    user_with_id = database[user_id - 1]

    return user_with_id


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):    
    """Use an id to update an user"""
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Invalid id'
        )
    user_with_id = UserDB(**user.model_dump(), id=user_id)

    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    """Use an id to delete an user"""
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Invalid id'
        )

    del database[user_id - 1]

    return {'message': 'User deleted with success'}
