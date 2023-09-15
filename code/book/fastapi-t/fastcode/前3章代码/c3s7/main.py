import typing

from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

"""
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": ["rock", "metal", "bar"]
}
"""

"""
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "image": {
        "url": "http://example.com/baz.jpg",
        "name": "The Foo live"
    }
}
"""

"""
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "images": [
        {
            "url": "http://example.com/baz.jpg",
            "name": "The Foo live"
        },
        {
            "url": "http://example.com/dave.jpg",
            "name": "The Baz"
        }
    ]
}
"""


class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float
    # tags: typing.List[str]
    image: typing.List[Image]


@app.post("/item")
def create_item(item: Item):
    print(item)

