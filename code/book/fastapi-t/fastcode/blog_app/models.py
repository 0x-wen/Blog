from sqlalchemy import Column, String, Integer, TEXT
from sqlalchemy.ext.declarative import declarative_base


BaseModel = declarative_base()


class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(255))
    password = Column(String(255))
    email = Column(String(255))


class Blog(BaseModel):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255))
    body = Column(TEXT())
