from typing import Optional
from fastapi import FastAPI

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