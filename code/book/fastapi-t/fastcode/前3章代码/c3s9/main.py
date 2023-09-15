import typing
import dataclasses
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()

"""
10
"""

"""
{
 "data": {
    "k1": "v1",
    "k3": "v2",
}

}
"""


# @app.post("/item")
# def create_item(item: int = Body()):
#     print(item)


# @app.post("/item")
# def create_item(item: typing.Dict[str, str]):
#     print(item)
#     return item


# @app.post("/item")
# def create_item(item: typing.List[str]):
#     print(item)
#     return item


# @app.post("/item")
# def create_item(item: typing.Set[str]):
#     print(item)
#     return item


@dataclasses.dataclass
class User:
    username: str
    password: str


@app.post("/item")
def create_item(user: User):
    return user