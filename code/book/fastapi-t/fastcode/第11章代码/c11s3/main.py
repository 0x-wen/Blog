from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse, PlainTextResponse


app = FastAPI(default_response_class=JSONResponse)			# 设置全局的默认响应方式
router = APIRouter(default_response_class=JSONResponse)		 # 设置APIRouter所有接口的默认响应方式


@app.get("/", response_class=JSONResponse)					# 设置这个接口的默认响应方式
def hello():
    return {"id": 1, "name": "liixu"}