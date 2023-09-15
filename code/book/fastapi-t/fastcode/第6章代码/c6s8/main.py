import typing
from fastapi import FastAPI, Form, File, UploadFile

app = FastAPI()


@app.post("/register")
def register(
        avatar: typing.Optional[bytes] = File(default=None),
        username: str = Form(),
        password: str = Form(min_length=6, max_length=10),
        accessary: typing.Optional[UploadFile] = None
):
    return {
        "username": username,
        "password": password,
        "avatar": len(avatar) if avatar else 0,
        "accessary": accessary.filename if accessary else ""
    }