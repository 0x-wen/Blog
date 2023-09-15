from fastapi import FastAPI, File


app = FastAPI()


@app.post("/upload")
def upload_file(file: bytes = File()):
    with open("abc.txt", "wb") as f:
        f.write(file)
    return file


# @app.post("/upload")
# async def upload_file(file=File()):
#     content = await file.read()		# 需要特殊处理才能过去文件的二进制数据
#     print(content)
#     return content
