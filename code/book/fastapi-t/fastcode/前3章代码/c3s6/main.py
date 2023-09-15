from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


# class User(BaseModel):
#     name: str
#     age: int
#
#
# @app.post("/login")
# def login(user: User):
#     return {"name": user.name, "age": user.age}

"""
{
  "name": "string",
  "age": 16
}
"""

@app.post("/login")
def login(name: str = Body(min_length=3), age: int = Body(ge=18)):
    return {"name": name, "age": age}
