from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Blog     # 自己在models中创建Blog


router = APIRouter()


@router.get("/blogs")
def get_blogs(db: Session = Depends(get_db)):
    # db.query(Blog).all()  自己完善接口
    pass


@router.get("/blog/{blog_id}")
def get_blog_by_id(blog_id: int):
    pass        # 自己完善接口内的db查询逻辑


