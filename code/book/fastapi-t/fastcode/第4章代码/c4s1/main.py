from http import HTTPStatus

from fastapi import FastAPI, status
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    username: str
    password: str


@app.post("/login", status_code=status.HTTP_201_CREATED)
def login(user: User):
    return {
        "username": user.username,
        "password": user.password,  # 真实项目中是不能返回用户密码的
    }
