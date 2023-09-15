from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    username: str
    password: str


class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float

"""
{
    "user": {
        "username": "liuxu",
        "password": "liuxu"
    },
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "importance": 5
}
"""
# @app.post("/login")
# def login(item: Item, user: User, importance: int = Body()):
#     print(user.username, user.password)
#     print(item.name, item.description)
#     print(importance)
#     pass



"""
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
"""


"""
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}
"""

@app.post("/login")
def login(item: Item = Body(embed=True)):
    print(item.name, item.description)
    pass
