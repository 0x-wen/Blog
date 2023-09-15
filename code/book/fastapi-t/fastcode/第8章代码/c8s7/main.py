import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


# 使用pymysql作为MySQLdb
pymysql.install_as_MySQLdb()

# 指定连接的MySQL数据库
DATABASE_URL = "mysql://root:12345@localhost:3306/db"

# 创建引擎
engine = create_engine(DATABASE_URL)

# 基于引擎创建session
SessionLocal = sessionmaker(bind=engine)

# 实例化session对象，得到db对象
db: Session = SessionLocal()


BaseModel = declarative_base()


class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    password = Column(String(255))


result = db.query(User).filter(User.id == 5).first()
print(result.id, result.name, result.password)

#  db使用只有需要关闭，避免占用资源
db.close()