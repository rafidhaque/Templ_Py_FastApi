import enum
from datetime import datetime
from typing import Optional, List
from fastapi import FastAPI, Request, Depends, Header
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr

from keycloak import KeycloakAdmin, KeycloakOpenID

from app.depends.auth_depend import get_current_user

router = InferringRouter()


class KeycloakUserRegistration(BaseModel):
    keycloak_user_id: str
    user_id: int
    account_ids: List[int]
    password: str
    domain_name: str
    company_name: str
    industry_name: str


@cbv(router)
class Keycloak:
    # user: CurrentUser = Depends(get_current_user)

    # 127.0.0.1
    # host.docker.internal
    # 172.17.0.1


    keycloak_openid = KeycloakOpenID(server_url="http://127.0.0.1:7003/auth/",
                    client_id="jwt-client", #new clreated inside dev realm
                    realm_name="dev",
                    client_secret_key="10687854-c643-4f58-81b1-02f2a0e0b1cb")

    # working from master
    # keycloak_admin = KeycloakAdmin(server_url="http://127.0.0.1:7003/auth/",
    #                            username='admin',
    #                            password='adminpass',
    #                            realm_name="master",
    #                            verify=False
    #                            )

    # keycloak_admin = KeycloakAdmin(server_url="http://127.0.0.1:7003/auth/",
    #                         username='dev-admin',
    #                         password='adminpass',
    #                         realm_name="master",
    #                         # user_realm_name="dev",
    #                         client_id="dev-realm",
    #                         client_secret_key="969518d1-182a-44de-85ac-9b5e98c4224d",
    #                         verify=False
    #                         )

    keycloak_admin = KeycloakAdmin(server_url="http://127.0.0.1:7003/auth/",
                            username='dev-admin-user',
                            password='adminpass',
                            realm_name="dev",
                            client_id="admin-client",
                            client_secret_key="2fa26308-2821-4d94-9911-4ea3e018127a",
                            verify=False
                            )

    @router.get("/registration")
    def get_list(self, token: str = Header(...)):
        user = self.keycloak_openid.userinfo(token)
        return { "token": token, "user": user}

    @router.post("/registration")
    def post_item(self, item: KeycloakUserRegistration):
        user_count =  self.keycloak_admin.users_count()
        user = self.keycloak_admin.get_user(item.keycloak_user_id)
        response = self.keycloak_admin.update_user(user_id=item.keycloak_user_id, 
                                      payload={
                                        "attributes": {
                                            "user_id": item.user_id,
                                            "account_ids": item.account_ids
                                        }
                                      })
        updated_user = self.keycloak_admin.get_user(item.keycloak_user_id)
        return { "item": item, "user": user, "user_count": user_count, "updated_user": updated_user }

    @router.post("/password")
    def post_password(self, user_id: str, password: str ):
        response = self.keycloak_admin.set_user_password(user_id=user_id, password=password, temporary=False)



    @router.get("/token")
    def get_token(self, user: str, password: str):
        token = self.keycloak_openid.token(user, password)        
        return {"user": user, "password": password, "token": token, "access_token": token["access_token"] }    

    @router.get("/user-from-token")
    def get_user_from_token(self, access_token: str = Header(...)):
        token_user = self.keycloak_openid.userinfo(access_token)


        # KEYCLOAK_PUBLIC_KEY = self.keycloak_openid.public_key()
        # options = {"verify_signature": True, "verify_aud": True, "verify_exp": True}
        # decode_user = self.keycloak_openid.decode_token(access_token, key=KEYCLOAK_PUBLIC_KEY, options=options)
        
        full_user = self.keycloak_admin.get_user(token_user["sub"])


        return { "access_token": access_token, "token_user": token_user, "full_user": full_user}







    
    @router.get("/data")
    def get_data(self, user = Depends(get_current_user)):
        return {"data": "able to access", "current_user": user }    
