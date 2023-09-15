import typing

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI(default_response_class=JSONResponse)


class User(BaseModel):
    username: str
    password: str
    re_password: str
    email: str


class UserOut(BaseModel):
    username: str
    email: str


@app.post("/register", response_model=UserOut)
def register(user: User):
    # 注册用户的操作, db
    # return {
    #     "username": user.username,
    #     "email": user.email,
    # }
    return user


@app.post("/demo", response_model=typing.Dict[str, str])
def demo():
    return {
        "name": "liuxu",
        "age": 18
    }

