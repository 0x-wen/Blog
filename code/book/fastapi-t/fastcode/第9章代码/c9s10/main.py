import typing
import datetime

import jwt
from jwt import PyJWTError
from sqlalchemy.orm import Session
from fastapi import FastAPI, Form, HTTPException, Depends, Header, Response, Cookie
from passlib.context import CryptContext

from schamas import UserOut
from database import get_db
from models import User

app = FastAPI()
crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")
secret_key = "897@4609{】（）——*90&*（"
exp = datetime.datetime.now() + datetime.timedelta(days=14)


@app.post("/register", response_model=UserOut)
def register(
        username: str = Form(),
        password: str = Form(),
        re_password: str = Form(),
        email: str = Form(),
        db: Session = Depends(get_db)
):
    if password != re_password:
        raise HTTPException(detail="两次密码输入不一致", status_code=400)

    db_user = db.query(User).filter(User.username == username).first()
    if db_user:
        raise HTTPException(detail="用户名已存在", status_code=400)

    user = User(
        username=username,
        password=crypt.hash(password),
        email=email
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@app.post("/login", response_model=UserOut)
def login(response: Response, username: str = Form(), password: str = Form(), db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == username).first()
    if not db_user:
        raise HTTPException(detail="用户名不存在", status_code=404)

    if not crypt.verify(password, db_user.password):
        raise HTTPException(detail="用户名或密码错误", status_code=400)

    # 签发jwt token
    payload = {"username": db_user.username, "exp": exp}
    jwttoken = jwt.encode(payload=payload, key=secret_key)
    response.set_cookie("jwttoken", jwttoken)
    # response.headers["x-jwttoken"] = jwttoken
    return db_user


@app.get("/books")
def books(jwttoken: typing.Optional[str] = Cookie(default=None), db: Session = Depends(get_db)):
    # jwt token解析
    try:
        user_info = jwt.decode(jwttoken, key=secret_key, algorithms="HS256")
    except PyJWTError:
        raise HTTPException(detail="Invalid jwttoken", status_code=403)
    username = user_info["username"]
    db_user = db.query(User).filter(User.username == username).first()
    if not db_user:
        raise HTTPException(detail="Invalid x_token", status_code=403)

    return [{"id": i + 1, "title": f"books{i}"} for i in range(10)]

