import aiomysql
from aiomysql.cursors import DictCursor

from fastapi import FastAPI


app = FastAPI(title="使用aiomysql")


async def aiomysql_demo():
    # 获取连接对象
    conn = await aiomysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="12345",
        db="db",
        cursorclass=DictCursor      # 返回字典格式的数据
    )
    # 创建游标
    cur = await conn.cursor()
    # 执行SQL
    await cur.execute("SELECT * from users;")
    # 获取SQL结果
    result = await cur.fetchall()
    # 关闭CURSOR
    await cur.close()
    # 关闭连接
    conn.close()

    return result


@app.get("/")
async def index():
    return await aiomysql_demo()
