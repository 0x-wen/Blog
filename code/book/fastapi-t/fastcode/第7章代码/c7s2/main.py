import typing
from fastapi import FastAPI, Depends

app = FastAPI()


def username_extractor(username: typing.Optional[str] = None):
    return username


def username_or_nickname_extractor(
    username: str = Depends(username_extractor),
    nickname: typing.Optional[str] = None
):
    if not username:
        return nickname
    return username


@app.get("/name")
def get_name(username_or_nickname: str = Depends(username_or_nickname_extractor)):
    return {"username_or_nickname": username_or_nickname}
