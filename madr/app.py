from fastapi import FastAPI

from madr.schemas import Message

app = FastAPI()


@app.get('/', response_model=Message)
def index_response():
    return {'message': 'home do projeto'}
