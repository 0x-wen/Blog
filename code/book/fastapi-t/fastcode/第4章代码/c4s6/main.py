from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5


@app.get("/item")
def read_item_name():
    item = Item(name="foo", description="desc", price=9.9)
    # return item.dict(include={"name"})
    # return item
    return item.dict(exclude_unset=True)
