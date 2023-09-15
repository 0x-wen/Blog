from fastapi import FastAPI


app = FastAPI()


@app.get("/apple")
def apple():
    return {"name": "apple", "price": 9.9}


@app.get("/huawei")
def huawei():
    return {"name": "huawei", "price": 99}


# @app.get("/books/1")
# def books():
#     return {"id": 1, "title": "图书1"}
#
#
# @app.get("/books/2")
# def books():
#     return {"id": 2, "title": "图书2"}


# 动态路由的解决方式
@app.get("/books/{book_id}")
def books(book_id: int):
    print(type(book_id))    # book_id = int(book_id)
    return {"id": book_id, "title": f"图书{book_id}"}