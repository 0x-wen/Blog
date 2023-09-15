from fastapi import FastAPI
from fastapi.responses import StreamingResponse, FileResponse

app = FastAPI()


@app.get("/")
def index():

    def iterfile():  #
        with open("mybook.zip", mode="rb") as f:  #
            yield from f

    return StreamingResponse(iterfile(), media_type="application/zip")


@app.get("/file")
def index():
    return FileResponse("mybook.zip", filename="123.zip") 	# 第一个参数文件路径，filename指定下载下来的文件名