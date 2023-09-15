from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session


import crud
from database import get_db
from schamas import UserOut, UserIn


app = FastAPI(title="FASTAPI + ORM")


@app.get("/users")
def get_users(page: int = 1, size: int = 3, db: Session = Depends(get_db)):
    return crud.get_users(page, size, db)


@app.get("/user/{user_id}", response_model=UserOut)
def ger_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_by_id(user_id, db)


@app.delete("/user/{user_id}")
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    crud.delete_user_by_id(user_id, db)
    return {"code": 200, "msg": "OK"}


@app.post("/user", response_model=UserOut)
def create_user(user: UserIn, db: Session = Depends(get_db)):
    return crud.create_user(user, db)


@app.put("/user/{user_id}", response_model=UserOut)
def update_user_by_id(user_id: int, user: UserIn, db: Session = Depends(get_db)):
    return crud.update_user(user_id, user, db)
