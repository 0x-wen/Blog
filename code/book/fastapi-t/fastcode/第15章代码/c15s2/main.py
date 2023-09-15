import time
from fastapi import FastAPI, Request

app = FastAPI()


# 定义的中间件函数必须是协程函数

# @app.middleware("http")
# async def process_time(request: Request, call_next):
#     print("123")
#     start_time = time.time()
#     response = await call_next(request)
#     print("456")
#     process_time = time.time() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     return response
#


@app.middleware("http")
async def middleware1(request: Request, call_next):
    print("mid1:请求来了")
    response = await call_next(request)
    print("mid1:响应走了")
    return response


@app.middleware("http")
async def middleware2(request: Request, call_next):
    print("mid2:请求来了")
    response = await call_next(request)
    print("mid2:响应走了")
    return response

@app.get("/")
async def index():
    print("index")
    return {"hello": "world"}
