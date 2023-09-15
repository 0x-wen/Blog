from fastapi import FastAPI, Depends

app = FastAPI()


BOOKS = [{"id": i, "name": f"book{i}", "status": i % 4 != 0} for i in range(1, 11)]


class CommonParams:
    def __init__(self, page: int, size: int, status: bool):
        self.page = page
        self.size = size
        self.status = status


@app.get("/api/books")
def get_books(commons: CommonParams = Depends()):
    page = commons.page
    size = commons.size
    status = commons.status
    books = [b for b in BOOKS if b["status"] == status]
    return books[(page - 1) * size:page * size]

