from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


BaseModel = declarative_base()


class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255))
    password = Column(String(255))
    email = Column(String(255))


    def __str__(self):
        return f"id: {self.id}, name: {self.username}, pwd: {self.password}"
