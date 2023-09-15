import hashlib

from fastapi import FastAPI, Form, HTTPException

app = FastAPI()

# 模拟数据库： {“jakc”: ....}
USERS = {}


@app.post("/register")
def register(
        username: str = Form(),
        password: str = Form(),
        re_password: str = Form(),
        email: str = Form(),
):
    if username in USERS:
        raise HTTPException(detail="用户名已存在", status_code=400)
    if password != re_password:
        raise HTTPException(detail="两次密码输入不一致", status_code=400)

    m = hashlib.md5("jiadasd324589230(*n3盐".encode("utf-8"))
    m.update(password.encode("utf-8"))
    hashed_password = m.hexdigest()      # 加密之后的密文

    USERS[username] = {
        "username": username,
        "password": hashed_password,
        "email": email
    }
    print(password)
    print(hashed_password)
    return {
        "username": username,
        "email": email
    }
