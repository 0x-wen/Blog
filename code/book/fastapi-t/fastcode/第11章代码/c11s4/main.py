from fastapi import FastAPI, Response
from fastapi.responses import PlainTextResponse, HTMLResponse

app = FastAPI()
#
#
# @app.get("/", response_class=PlainTextResponse)
# def main():
#     return "Hello World"



@app.get("/")
def main():
    # response = Response(
    #     content="HELLO WORLD",
    #     media_type="text/plain"
    # )
    # return response
    return PlainTextResponse(content="HELLO WORLD")




@app.get("/html",  response_class=HTMLResponse)
def index():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)