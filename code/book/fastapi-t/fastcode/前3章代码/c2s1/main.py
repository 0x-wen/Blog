from fastapi import FastAPI


app = FastAPI()


@app.get("/books/{book_id:int}")    # 路径转换器
def books(book_id):
    print(type(book_id))
    return {"id": book_id, "title": f"图书{book_id}"}


# /files/data/abc.txt
@app.get("/files/{file_path:path}")
def read_file(file_path: str):
    # open file
    with open(file_path, "rb") as f:
        content = f.read()
    return content
