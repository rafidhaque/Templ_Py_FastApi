import enum
from datetime import datetime
from typing import Optional, List
from fastapi import FastAPI, Request, Depends, Header
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from fastapi.responses import JSONResponse


router = InferringRouter()


@cbv(router)
class Keycloak:
    
    @router.get("/data")
    def get_data(self):
        return {"data": "able to access" }    
