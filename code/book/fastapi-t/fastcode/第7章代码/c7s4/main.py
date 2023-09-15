from fastapi import Depends, FastAPI, Header, HTTPException


def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    # return x_token


app = FastAPI(dependencies=[Depends(verify_token)])



# @app.get("/items", dependencies=[Depends(verify_token)])
# def get_items():
#     return [{"item": "Foo"}, {"item": "Bar"}]
#


@app.get("/items")
def get_items():
    return [{"item": "Foo"}, {"item": "Bar"}]

