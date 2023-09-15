from fastapi import FastAPI, HTTPException, status

from routers import blog, user


app = FastAPI(title="Blog CRUD")

app.include_router(blog.router, tags=["Blog"])
app.include_router(user.router, tags=["User"], prefix="/user")



