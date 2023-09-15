from fastapi import FastAPI


app = FastAPI()


@app.get("/books/most_popular")    # /books/most_popular
def most_popular():
    return {"data": "这是本站最畅销的图书"}


# 动态路由的解决方式
@app.get("/books/{book_id}")    # /books/most_popular
def books(book_id: int):
    return {"id": book_id, "title": f"图书{book_id}"}
