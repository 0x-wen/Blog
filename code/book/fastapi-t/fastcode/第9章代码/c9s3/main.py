from sqlalchemy.orm import Session
from fastapi import FastAPI, Form, HTTPException, Depends
from passlib.context import CryptContext

from schamas import UserOut
from database import get_db
from models import User

app = FastAPI()
crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")


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



