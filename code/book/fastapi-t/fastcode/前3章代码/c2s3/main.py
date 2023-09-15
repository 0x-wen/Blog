from fastapi import FastAPI, Path


app = FastAPI()


@app.get("/blogs/{id}")
def get_blogs_by_id(id: int = Path(gt=2, le=10)):
    return id


@app.get("/blogs/{name}")
def get_blogs_by_name(name: str = Path(min_length=5, max_length=10)):
    return name
