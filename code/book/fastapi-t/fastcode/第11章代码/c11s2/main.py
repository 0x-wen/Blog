import json
from fastapi import FastAPI, Response
from starlette.responses import Response


app = FastAPI()


@app.get("/", )
def hello():
    response = Response(
        content=json.dumps({"hello": "world"}),
        status_code=201,
        headers={"x-token": "qqqqqq"},
        media_type="application/json"
    )

    return response
