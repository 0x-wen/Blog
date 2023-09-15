from fastapi import FastAPI, Request, Query, Path,Header
# from starlette.requests import Request


app = FastAPI()


@app.get("/{item_id}")
def hello(item_id: int, req: Request, page: int):
    print(item_id)
    print(page)
    item_id = req.path_params.get("item_id")
    page = req.query_params.get("page", 0)
    size = req.query_params.get("size", 10)
    x_token = req.headers.get("x-token")
    x_token_cookie = req.cookies.get("x_token")

    return {
        "item_id": item_id,
        "page": page,
        "size": size,
        "x-token": x_token,
        "cookie": x_token_cookie,
        "client_host": req.client.host,
    }