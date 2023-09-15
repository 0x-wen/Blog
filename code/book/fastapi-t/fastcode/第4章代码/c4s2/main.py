from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    username: str
    password: str


# @app.post("/login")
# def login(user: User, response: Response):
#     response.headers["x-jwt-token"] = "this_is_jwttoken"
#     response.headers.append("x-token", "value")
#     return {
#         "username": user.username,
#         "password": user.password,  # 真实项目中是不能返回用户密码的
#     }


@app.post("/login")
def login(user: User):
    response = JSONResponse(
        {
            "username": user.username,
            "password": user.password,
        },
        status_code=201,
        headers={"x-jwt-token": "value"}
    )

    return response
