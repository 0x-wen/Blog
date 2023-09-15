from pydantic import BaseModel


# user
class UserBase(BaseModel):
    username: str
    email: str


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True


# blog
class BlogBase(BaseModel):
    title: str
    body: str


class BlogIn(BlogBase):
    pass


class BlogOut(BlogBase):
    id: int

    class Config:
        orm_mode = True
