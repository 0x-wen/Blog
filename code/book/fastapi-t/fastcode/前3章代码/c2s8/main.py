import typing
from fastapi import FastAPI, Query, Path


app = FastAPI()


@app.get("/items/{name}")
def info(age: int = Query(ge=18), name: str = Path(default=None, min_length=3)):
    return {
        "name": name,
        "age": age
    }
