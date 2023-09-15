from fastapi import Depends, FastAPI


app = FastAPI()


def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()



@app.get("/books")
def books(db: Depends(get_db)):
    db.execute("select * form books")   # db操作
    pass

#
# @app.get("/books")
# def books():
#     db = DBSession()
#     db.execute("select * form books")   # db操作
#     db.close()
#
#
#     pass
