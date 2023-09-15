from fastapi import APIRouter, Form, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas import UserOut
from models import User
from database import get_db
from tools import jwt_obj, hash_obj


router = APIRouter()


class UserForm:
    def __init__(self, username: str = Form(), password: str = Form(), re_password: str = Form(), email: str = Form()):
        self.username = username
        self.password = password
        self.re_password = re_password
        self.email = email


@router.post("/register", response_model=UserOut)
def register(user: UserForm = Depends(), db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(detail="用户名已存在", status_code=400)
    if user.password != user.re_password:
        raise HTTPException(detail="两次密码输入不一致", status_code=400)

    new_user = User(
        username=user.username,
        password=hash_obj.hash(user.password),
        email=user.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login")
def login(username: str = Form(), password: str = Form(), db: Session = Depends(get_db)):
    db_user: User = db.query(User).filter_by(username=username).first()
    if not db_user:
        raise HTTPException(detail="用户名不存在", status_code=400)
    if not hash_obj.verify(password, db_user.password):
        raise HTTPException(detail="用户名或密码错误", status_code=400)

    # 签发jwt token
    access_token = jwt_obj.set_token({"id": db_user.id, "name": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}
