import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from fastapi import FastAPI, Depends, HTTPException


pymysql.install_as_MySQLdb()

DATABASE_URL = "mysql://root:12345@localhost:3306/db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


BaseModel = declarative_base()


class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    password = Column(String(255))

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, pwd: {self.password}"


app = FastAPI(title="FASTAPI + ORM")


@app.get("/users")
def get_users(page: int = 1, size: int = 3, db: Session = Depends(get_db)):
    users = db.query(User).all()
    users = users[(page - 1) * size: page * size]
    return [{"id": u.id, "name": u.name} for u in users]
    # return users


@app.get("/user/{user_id}")
def ger_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(detail="Not found", status_code=404)
    return user


@app.delete("/user/{user_id}")
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db.query(User).filter_by(id=user_id).delete()
    db.commit()
    return {"code": 200, "msg": "OK"}