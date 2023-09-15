import typing
from fastapi import FastAPI, Query


app = FastAPI()


# @app.get("/items")
# def info(name: str = Query(min_length=3, max_length=10), age: int = Query(ge=18)):
#     return {"name": name, "age": age}

#
# @app.get("/items")
# def info(name: typing.Optional[str] = Query(default=None)):
#     return {"name": name}


# 设置参数是必选的
@app.get("/items")
def info(name: typing.Optional[str] = Query(default=...)):
    return {"name": name}
