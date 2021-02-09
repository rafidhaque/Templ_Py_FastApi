from typing import Optional
from fastapi import APIRouter

from app.errors import UnicornException

router = APIRouter()

@router.get("/error")
async def get_list():
    raise UnicornException(name="Not managed error.")


@router.get("/error/{item_id}")
def get_item(item_id: int, q: Optional[str] = None):
    raise Exception("Not managed error.")


@router.put("/error/{item_id}")
def put_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@router.post("/error/{item_id}")
def post_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@router.delete("/error/{item_id}")
def delete_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}