import datetime

from jose import jwt, JWTError
from fastapi import FastAPI, Form, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer


app = FastAPI()
secret_key = "scnmwoeijcnwd"
exp = datetime.datetime.now() + datetime.timedelta(days=1)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@app.post("/login")
def login(username: str = Form(), password: str = Form()):
    if not username or not password:
        raise HTTPException(detail="login failed", status_code=404)

    # 简化数据库操作
    # 直接签发 jwt token
    payload = {"username": username, "exp": exp}
    access_token = jwt.encode(payload, secret_key, "HS256")
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@app.get("/books")
def get_books(token: str = Depends(oauth2_scheme)):
    try:
        data = jwt.decode(token, key=secret_key, algorithms="HS256")
        return [{"id": i + 1} for i in range(10)]
    except JWTError:
        raise HTTPException(detail="invalid jwt token", status_code=403)
