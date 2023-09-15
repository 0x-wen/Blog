import typing
from fastapi import FastAPI, Query, Path, Header


app = FastAPI()


# @app.get("/books")
# def get_books(token: str = Header()):
#     return token


# @app.get("/books")
# def get_books(token: typing.List[str] = Header()):
#     return token


@app.get("/books")
def get_books(x_token: typing.List[str] = Header(convert_underscores=True)):
    return x_token
