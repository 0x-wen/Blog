from typing import Union
import json
from datetime import datetime
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    timestamp: datetime


@app.post("/item")
def create_item(item: Item):
    print(item)
    jsonable_item = jsonable_encoder(item)
    print(jsonable_item)
    json_item = json.dumps(jsonable_item)
    print(json_item)
    return item
