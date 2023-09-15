from fastapi import FastAPI, Path


app = FastAPI()

examples = {
    "valid": {"value": 20},
    "invalid": {"value": 8},
}


@app.get("/blogs/{id}")
def get_blogs_by_id(id: int = Path(
    description="这是根据id找找blog的接口",
    example="100",
    examples=examples,
    # deprecated=True,
    include_in_schema=False
)):
    return id


@app.get("/blogs/{name}")
def get_blogs_by_name(name: str = Path(min_length=5, max_length=10)):
    return name
