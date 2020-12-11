from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse
from loguru import logger

from app.api import item_api, user_api, employee_api, error_api, keycloak_api, keycloak_auth_api
from app.errors import UnicornException
from app.depends.auth_depend import get_current_user


app = FastAPI()





async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


# https://fastapi.tiangolo.com/tutorial/handling-errors/
@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    # print(f"OMG! An HTTP error!: {repr(exc)}")
    return JSONResponse(
        status_code=500,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )

@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    # print(f"OMG! An HTTP error!: {repr(exc)}")
    logger.add("file_{time}.log")
    logger.error(exc)

    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"},
    )


app.include_router(error_api.router)
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
app.include_router(
    keycloak_api.router,
    prefix="/keycloak",
    tags=["Keycloak"]
)
app.include_router(
    keycloak_auth_api.router,
    dependencies=[Depends(get_current_user)],
    prefix="/keycloak-Auth",
    tags=["Keycloak-Auth"]
)