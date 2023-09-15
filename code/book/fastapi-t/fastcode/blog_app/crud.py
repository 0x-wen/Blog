import typing

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import Blog
from schemas import BlogIn


def get_blogs(page: int, size: int, db: Session) -> typing.List[Blog]:
    blogs: typing.List[Blog] = db.query(Blog).all()[(page - 1) * size:page * size]
    return blogs


def get_blog_by_id(blog_id: int, db: Session) -> Blog:
    blog: Blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(detail=f"Not found blog with id: {blog_id}", status_code=404)
    return blog


def delete_blog_by_id(blog_id: int, db: Session):
    db.query(Blog).filter(Blog.id == blog_id).delete()


def create_blog(blog: BlogIn, db: Session) -> Blog:
    db_blog = Blog(**blog.dict())
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)  # refresh之后，db_blog才有数据
    return db_blog


def update_blog(blog_id: int, blog: BlogIn, db: Session) -> Blog:
    db_blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if not db_blog:
        raise HTTPException(detail=f"Not found user with id: {blog_id}", status_code=404)
    db_blog.title = blog.title
    db_blog.body = blog.body
    db.commit()
    db.refresh(db_blog)
    return db_blog
