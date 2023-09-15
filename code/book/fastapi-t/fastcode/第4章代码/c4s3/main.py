from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI(default_response_class=JSONResponse)


class User(BaseModel):
    username: str
    password: str


# @app.get("/")
# def hello():
#     return [{"id": i, "name": f"图书{i}"} for i in range(10)]
#

# @app.post("/login")
# def login(user: User):
#     return user.dict()


@app.post("/login")
def login(user: User):
    response = JSONResponse(content="12345")
    return response


