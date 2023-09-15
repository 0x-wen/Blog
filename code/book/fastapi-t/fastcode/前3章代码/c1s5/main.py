import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")       # 路径(函数)装饰器
def hello():        # 路径函数，接口函数
    return {"hello": "worldqqqqq"}


if __name__ == '__main__':
    uvicorn.run("main:app", port=9090, reload=True)
