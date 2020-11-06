from typing import Optional
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.errors import UnicornException

app = FastAPI()



@app.get("/hello")
def get_list():
    return {"Hello": "World"}

@app.get("/hello/{item_id}")
def get_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/hello/{item_id}")
def put_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post("/hello/{item_id}")
def post_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.delete("/hello/{item_id}")
def delete_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}





# ----------------------------------------- Error --------------------------------------------------
@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    # print(f"OMG! An HTTP error!: {repr(exc)}")
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )

@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    # print(f"OMG! An HTTP error!: {repr(exc)}")
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"},
    )

@app.get("/error")
def error_list():
    raise UnicornException(name="Not managed error.")

@app.get("/error/{item_id}")
def error():
    raise Exception("Not managed error.")