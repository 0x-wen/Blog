from fastapi import FastAPI
from fastapi.responses import RedirectResponse, ORJSONResponse, JSONResponse

app = FastAPI()


@app.get("/about")
def index():
    return RedirectResponse("/index")


@app.get("/baidu")
def go_to_baidu():
    return RedirectResponse("https://www.baidu.com")


@app.get("/index")
def index():
    return "index"
