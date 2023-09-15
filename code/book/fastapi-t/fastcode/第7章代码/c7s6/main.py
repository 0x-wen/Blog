from fastapi import FastAPI, Depends

app = FastAPI()


class FixedContentQueryChecker:
    def __init__(self, fix_content: str):
        self.fix_content = fix_content

    def __call__(self, q: str) -> bool:
        return self.fix_content in q


hello = FixedContentQueryChecker("hello")
world = FixedContentQueryChecker("world")


@app.get("/hello")
def hello_check(exists: bool = Depends(hello)):
    return {"exists": exists}


@app.get("/world")
def hello_check(exists: bool = Depends(world)):
    return {"exists": exists}

