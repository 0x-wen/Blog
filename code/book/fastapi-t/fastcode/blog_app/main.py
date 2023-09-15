from fastapi import FastAPI

from routers import user, blog


app = FastAPI(title="APIRouter demo")


app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(blog.router, prefix="/blog", tags=["Blog"])
