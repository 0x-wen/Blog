import pymysql

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

pymysql.install_as_MySQLdb()


DATABASE_URL = "mysql://app:app@mysql:3306/app"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()

