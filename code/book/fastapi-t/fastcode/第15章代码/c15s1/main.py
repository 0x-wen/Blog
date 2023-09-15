from fastapi import FastAPI

app = FastAPI()

items = {}


@app.on_event("startup")
async def startup_event():
    items["foo"] = {"name": "Fighters"}
    items["bar"] = {"name": "Tenders"}
    print("startup_event run...")


@app.on_event("startup")
def pp():
    print("this is pp run...")


@app.on_event("shutdown")
def shutdown_event1():
    print("1关机了....")


@app.on_event("shutdown")
async def shutdown_event2():
    print("2关机了....")


@app.get("/items/{item_id}")
async def read_items(item_id: str):
    return items[item_id]