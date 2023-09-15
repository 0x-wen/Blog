from fastapi import FastAPI
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
}
"""
@app.post("/login")
def login(item: Item, user: User):
    print(user.username, user.password)
    print(item.name, item.description)
    pass
