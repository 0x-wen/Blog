import time
import asyncio
from fastapi import FastAPI

app = FastAPI()


# @app.get("/")
# def index():
#     time.sleep(5)
#     return "index"

# import time
# from fastapi import FastAPI
#
# app = FastAPI()


# @app.get("/")
# async def index():
#     await asyncio.sleep(5)
#     return "index"


@app.get("/")
async def index():
    time.sleep(5)
    return "index"

