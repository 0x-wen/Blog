from fastapi import FastAPI
from databases import Database


app = FastAPI(title="使用databases")


async def databases_demo():
    # 实例化一个db连接并建立连接
    database = Database('mysql://root:12345@localhost:3306/db')
    await database.connect()

    # Run a database query.
    query = "SELECT * FROM users"
    rows = await database.fetch_all(query=query)
    return rows


@app.get("/")
async def index():
    return await databases_demo()