import typing
from fastapi import FastAPI, Query


app = FastAPI()


BOOKS = [
    {"id": i, "title": f"图书{i}"}
    for i in range(1, 11)
]


# 错误的顺序
# @app.get("/books")
# def get_books(page: int, sort: bool, size: int = 4):
#     results = BOOKS[(page - 1) * size:page * size]
#     if sort:
#         results.sort(key=lambda x: x["id"])
#     return results


@app.get("/books")
def get_books(id: typing.List[int] = Query()):
    return id