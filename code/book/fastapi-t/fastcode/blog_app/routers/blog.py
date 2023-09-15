import typing
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from schemas import BlogOut, BlogIn
from database import get_db
from models import Blog
from tools import jwt_obj
import crud


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")


@router.get("/blogs", response_model=typing.List[BlogOut])
def get_blogs(page: int = 1, size: int = 3, db: Session = Depends(get_db)):
    blogs = crud.get_blogs(page, size, db)
    return blogs


@router.get("/blog/{blog_id}", response_model=BlogOut)
def get_blog_by_id(blog_id: int, db: Session = Depends(get_db)):
    blog: Blog = crud.get_blog_by_id(blog_id, db)
    return blog


@router.delete("/blog/{blog_id}")
def delete_blog_by_id(blog_id: int, db: Session = Depends(get_db),  token: str = Depends(oauth2_scheme)):
    data = jwt_obj.get_token(token)
    if data:
        crud.delete_blog_by_id(blog_id, db)
    return {"code": 1, "msg": "success"}


@router.post("/blog", response_model=BlogOut)
def create_blog(blog: BlogIn, db: Session = Depends(get_db),  token: str = Depends(oauth2_scheme)):
    data = jwt_obj.get_token(token)
    if data:
        return crud.create_blog(blog, db)


@router.put("/blog/{blog_id}", response_model=BlogOut)
def update_blog_by_id(blog_id: int, blog: BlogIn, db: Session = Depends(get_db)):
    return crud.update_blog(blog_id, blog, db)
