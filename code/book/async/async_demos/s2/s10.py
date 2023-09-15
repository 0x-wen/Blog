from fastapi import FastAPI
import uvicorn


aaaa = FastAPI()


@aaaa.get("/")
def root():
    return "hello world"


@aaaa.get("/index")
async def index123():
    return [1, 2, 3, 4, 5, 6]


uvicorn.run(aaaa)

