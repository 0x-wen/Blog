from fastapi import FastAPI, Depends

app = FastAPI()


BOOKS = [{"id": i, "name": f"book{i}", "status": i % 4 != 0} for i in range(1, 11)]
USERS = [{"id": i, "name": f"user{i}", "status": i % 4 != 0} for i in range(1, 11)]


def common_params(page: int = 1, size: int = 2, status: bool = True):
    return {
        "page": page,
        "size": size,
        "status": status
    }


@app.get("/api/books")
def get_books(commons: dict = Depends(common_params)):
    page = commons["page"]
    size = commons["size"]
    status = commons["status"]
    books = [b for b in BOOKS if b["status"] == status]
    return books[(page - 1) * size:page * size]


@app.get("/api/users")
def get_users(commons: dict = Depends(common_params)):  # 需要重复再次定义三个参数
    page = commons["page"]
    size = commons["size"]
    status = commons["status"]
    users = [u for u in USERS if u["status"] == status]
    return users[(page - 1) * size:page * size]
