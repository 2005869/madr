from fastapi import FastAPI

from madr.routers import users
from madr.schemas import Message

app = FastAPI()

app.include_router(users.router)


@app.get('/', response_model=Message)
def index_response():
    return {'message': 'home do projeto'}
