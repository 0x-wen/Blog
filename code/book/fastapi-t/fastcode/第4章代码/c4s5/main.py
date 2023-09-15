from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.get(
    "/items/{name}",
    response_model=Item,
    # response_model_include={"name", "tax"},
    # response_model_exclude={"name"},
    # response_model_exclude_unset=True,
    # response_model_exclude_defaults=True,
    response_model_exclude_none=True,
)
def read_item_name(name: str):
    return items[name]