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


# db.add(User(name="LX", password="12345"))
# db.add(User(name="LX2", password="12345"))
# db.commit()     # 非常重要的


# user3 = User(name="LX3", password="12345")
# user4 = User(name="LX4", password="12345")
# db.add_all([user3, user4])
# db.commit()


user5 = User(name="LX5", password="12345")
user6 = User(name="LX6", password="12345")
db.bulk_save_objects([user5, user6])
db.commit()

db.close()