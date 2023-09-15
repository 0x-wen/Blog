import asyncio
import aiohttp

from fastapi import FastAPI

app = FastAPI()


# 协程函数
async def aiohttp_demo():
    # 获取一个连接session
    async with aiohttp.ClientSession() as session:
        # 基于连接发送一个get请求并获取像一个response
        async with session.get('http://www.baidu.com') as response:
            # 从response中获取响应的各种结果
            # 因为基于上下文管理器，所以出自动关闭连接
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")
            return html


@app.get("/")
async def baidu():
    return await aiohttp_demo()
