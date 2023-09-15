from fastapi import FastAPI

from routers import user, blog


app = FastAPI(title="FASTAPI + ORM")

app.include_router(user.router, tags=["User"])
app.include_router(blog.router, tags=['Blog'])
