from fastapi import APIRouter, HTTPException, status


router = APIRouter()

# mock db
blogs = {
    1: {
        "id": 1,
        "title": "blog1"
    },
    2: {
        "id": 2,
        "title": "blog2"
    }
}


@router.get("/blog/blogs")
def get_blogs(page: int = 1, size: int = 10):
    blogs_list = list(blogs.values())
    return blogs_list[(page - 1) * size:page * size]


@router.get("/blog/{blog_id}")
def get_blog_by_id(blog_id: int):
    blog = blogs.get(blog_id)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found the blog with id: {blog_id}"
        )
    return blog
