from fastapi import Depends, FastAPI, Header, HTTPException

from app.api import item_api, user_api, employee_api

app = FastAPI()


async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


app.include_router(user_api.router)
app.include_router(
    item_api.router,
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)
app.include_router(
    employee_api.router,
    prefix="/employees",
    tags=["employees"],
)