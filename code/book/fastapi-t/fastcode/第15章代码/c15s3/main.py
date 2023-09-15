import time
import asyncio
from fastapi import FastAPI, BackgroundTasks


app = FastAPI()


# 模拟发邮件的服务
async def email_notify(user: str, msg: str):
    # time.sleep(5)   # 模拟发邮件耗时5s
    await asyncio.sleep(5)
    print(f"send to {user} a msg: {msg}")


@app.get("/")
def send_notify(bgt: BackgroundTasks):
    print("this is api run...")
    bgt.add_task(email_notify, "xm", msg="hello world")
    bgt.add_task(email_notify, "xm", msg="hello world")
    return {"data": "ok"}
