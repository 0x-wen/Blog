import typing

from fastapi import FastAPI, UploadFile, File, Form


app = FastAPI()


# @app.post("/upload")
# def upload_file(file: UploadFile = File(default=None)):
#     if not file:
#         return {"data": "no file"}
#     else:
#         return file.filename


# @app.post("/upload")
# def upload_file(username: str = Form(), file: UploadFile = File(default=None)):
#     if not file:
#         return {"data": "no file"}
#     else:
#         return file.filename
#

# @app.post("/upload")
# def upload_file(file: bytes = File(default=None)):
#     if not file:
#         return {"data": "no file"}
#     else:
#         return len(bytes)
#


@app.post("/upload")
def upload_file(file: typing.Optional[UploadFile] = None):
    if not file:
        return {"data": "no file"}
    else:
        return len(bytes)

