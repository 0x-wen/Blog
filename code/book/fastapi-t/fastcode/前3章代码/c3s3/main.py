from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    username: str
    password: str
    age: int


# user = User(username="liuxu", password="123456789)
@app.post("/login")
def login(user: User):
    print(type(user))
    return {
        "name": user.username
    }

