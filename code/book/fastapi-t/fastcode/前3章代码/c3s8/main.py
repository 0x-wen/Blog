import typing

from fastapi import FastAPI
from pydantic import BaseModel, Field

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


class Item(BaseModel):
    name: str = Field(min_length=5)
    description: str
    price: float = Field(ge=10)
    tax: float
    tags: typing.List[str] = Field(min_items=3, max_items=5, unique_items=True)


@app.post("/item")
def create_item(item: Item):
    print(item)

