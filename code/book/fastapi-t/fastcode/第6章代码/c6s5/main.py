from fastapi import FastAPI, UploadFile, File


app = FastAPI()


@app.post("/upload")
def upload_file(file: UploadFile = File()):
    content = file.file.read()  # 可以直接使用文件的操作方法
    file.file.close()

    return {
        "filename": file.filename,  # filename 是文件名 如：a.txt
        "type": file.content_type,  # content_type 是文件类型 如：text/plain
        "content": content  # file是标准的Python文件对象，可以直接使用文件的操作
    }

