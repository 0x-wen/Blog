from enum import Enum
from fastapi import FastAPI


app = FastAPI()


class TagName(str, Enum):
    PYTHON = "python"
    LINUX = "linux"
    WEB = "web"


@app.get("/blogs/{tag}")
def get_blogs_by_tag(tag: TagName):
    print(tag.name)
    print(tag.value)
    if tag == TagName.PYTHON:
        return "some blogs about python"
    elif tag.value == "web":
        return "some blogs about web"
    else:
        return "some blogs about linux"
