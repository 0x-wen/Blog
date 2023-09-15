import typing

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()

"""
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
}
"""


# class Item(BaseModel):
#     name: str = Field(min_length=5)
#     description: str
#     price: float = Field(ge=10)
#     tax: float
#
#     class Config:
#         schema_extra = {
#             "example": {
#                 "name": "Foo",
#                 "description": "this is a desc",
#                 "price": 9.9,
#                 "tax": 0.5
#             }
#         }


# class Item(BaseModel):
#     name: str = Field(min_length=5, example="Bar")
#     description: str = Field(example="THIS IS DESC")
#     price: float = Field(ge=10, example=100)
#     tax: float = Field(example=0.9)


class Item(BaseModel):
    name: str = Field(min_length=5)
    description: str
    price: float = Field(ge=10)
    tax: float


@app.post("/item")
def create_item(
    *,
    item: Item = Body(
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item works correctly.",
                "value": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
            },
            "converted": {
                "summary": "An example with converted data",
                "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                "value": {
                    "name": "Bar",
                    "price": "35.4",
                },
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "value": {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            },
        },
    ),
):
    return item