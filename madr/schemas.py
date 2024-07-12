from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    firstname: str
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    firstname: str
    username: str
    email: EmailStr
    id: int


class UserDB(UserSchema):
    id: int
