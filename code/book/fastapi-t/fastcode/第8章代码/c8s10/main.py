import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


pymysql.install_as_MySQLdb()


BaseModel = declarative_base()


class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    password = Column(String(255))

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, pwd: {self.password}"


DATABASE_URL = "mysql://root:12345@localhost:3306/db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
db: Session = SessionLocal()


# user: User = db.query(User).filter(User.id == 1).first()
# print(user)
# user.name = "LIUXU"
# db.commit()


# db.query(User).filter(User.id == 1).update({"name": "liuxu111", "password": "121"})
# db.commit()

db.query(User).filter_by(id=1).delete()
db.commit()


db.close()