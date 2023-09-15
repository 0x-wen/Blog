from fastapi import FastAPI


app = FastAPI()


BOOKS = [
    {"id": 1, "title": "图书1"},
    {"id": 2, "title": "图书2"},
    {"id": 3, "title": "图书3"},
    {"id": 4, "title": "图书4"},
    {"id": 5, "title": "图书5"},
    {"id": 6, "title": "图书6"},
    {"id": 7, "title": "图书7"},
    {"id": 8, "title": "图书8"},
    {"id": 9, "title": "图书9"},
    {"id": 10, "title": "图书10"},
]


@app.get("/books")
def books(page: int, size: int):
    # page=1, size=3 BOOKS[0:3]  0 1 2
    return BOOKS[(page - 1) * size: page * size]
