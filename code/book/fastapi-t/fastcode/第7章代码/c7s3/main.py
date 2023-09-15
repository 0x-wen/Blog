from fastapi import Depends, FastAPI

app = FastAPI()


# def get_num(num: int):
#     print("get_num被执行了")
#     return num


# @app.get("/")
# async def get_results(num1: int = Depends(get_num), num2: int = Depends(get_num, use_cache=False)):
#     return {"num1": num1, "num2": num2}


def get_num(num: int):
    print("get_num被执行了")
    return num


def get_result1(num: int = Depends(get_num)):
    return num


def get_result2(num: int = Depends(get_num, use_cache=False)):
    return num


@app.get("/")
def get_results(result1: int = Depends(get_result1), result2: int = Depends(get_result2)):
    return {
        "result1": result1,
        "result2": result2,
    }
