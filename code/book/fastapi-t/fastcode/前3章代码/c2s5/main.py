import typing
from fastapi import FastAPI


app = FastAPI()


BOOKS = [
    {"id": i, "title": f"图书{i}"}
    for i in range(1, 11)
]


@app.get("/books")
def books(q: typing.Optional[str] = None, page: int = 1, size: int = 3):
    if q:
        return BOOKS
    # page=1, size=3 BOOKS[0:3]  0 1 2
    return BOOKS[(page - 1) * size: page * size]
