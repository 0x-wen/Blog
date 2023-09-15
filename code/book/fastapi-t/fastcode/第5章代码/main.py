import typing

from fastapi import FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI(title="Blog CRUD")


# mock db
blogs = {
    1: {
        "id": 1,
        "title": "blog1",
        "body": "this is blog1",
        "desc": "desc"
    },
    2: {
        "id": 2,
        "title": "blog2",
        "body": "this is blog2",
        "desc": "desc"
    }
}
# blogs = [
#     {
#         "id": 1,
#         "title": "blog1",
#         "body": "this is blog1",
#         "desc": "desc"
#     },
#     {
#         "id": 2,
#         "title": "blog2",
#         "body": "this is blog2",
#         "desc": "desc"
#     }
# ]


class Blog(BaseModel):
    title: typing.Optional[str] = None
    body: typing.Optional[str] = None
    desc: str


@app.get("/blogs", tags=["Blog"])
def get_blogs(page: int = 1, size: int = 10):
    blogs_list = list(blogs.values())
    return blogs_list[(page - 1) * size:page * size]


@app.get("/blog",  tags=["Blog"])
def get_blog_by_id(blog_id: int):
    blog = blogs.get(blog_id)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found the blog with id: {blog_id}"
        )
    return blog


@app.post("/blog",  tags=["Blog"])
def create_blog(blog: Blog):
    blog_id = len(blogs) + 1
    blogs[blog_id] = {"id": blog_id, **jsonable_encoder(blog)}
    return blogs[blog_id]


@app.put("/blog",  tags=["Blog"])
def update_blog(blog_id: int, blog: Blog):
    to_update_blog = blogs.get(blog_id)
    if not to_update_blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found the blog with id: {blog_id}"
        )
    to_update_blog.update(jsonable_encoder(blog))
    blogs[blog_id] = to_update_blog
    return to_update_blog


@app.patch("/blog",  tags=["Blog"])
def update_blog2(blog_id: int, blog: Blog):
    to_update_blog = blogs.get(blog_id)
    if not to_update_blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found the blog with id: {blog_id}"
        )
    to_update_blog.update(**jsonable_encoder(blog, exclude_unset=True))
    blogs[blog_id] = to_update_blog
    return to_update_blog


@app.delete("/blog",  tags=["Blog"])
def delete_blog(blog_id: int):
    if not blogs.get(blog_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found the blog with id: {blog_id}"
        )
    return blogs.pop(blog_id, None)


