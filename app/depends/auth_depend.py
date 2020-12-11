from fastapi import FastAPI, Request, APIRouter, Depends, Header, HTTPException
from keycloak import KeycloakAdmin, KeycloakOpenID
from typing import Optional, List


class CurrentUser:
    id: int
    account_id: List[int]


def get_current_user(token: str = Header(...)):

    # check if header is empty
    # if authorization != "fake-super-secret-token":
    #     raise HTTPException(status_code=400, detail="token header invalid")

    keycloak_openid = KeycloakOpenID(server_url="http://127.0.0.1:7003/auth/",
                client_id="jwt-client", #new clreated inside dev realm
                realm_name="dev",
                client_secret_key="10687854-c643-4f58-81b1-02f2a0e0b1cb")

    keycloak_admin = KeycloakAdmin(server_url="http://127.0.0.1:7003/auth/",
                        username='dev-admin-user',
                        password='adminpass',
                        realm_name="dev",
                        client_id="admin-client",
                        client_secret_key="2fa26308-2821-4d94-9911-4ea3e018127a",
                        verify=False
                        )
    user = None
    full_user = None
    try:
        user = keycloak_openid.userinfo(token)
        # full_user = keycloak_admin.get_user("fb44a3c7-f5c0-4afc-a92f-2a2ae17421e3")
        full_user = keycloak_admin.get_user(user['sub'])
    except:
        raise HTTPException(status_code=403, detail="Invalid token")

    attr = full_user["attributes"]
    newUser = CurrentUser()
    newUser.user_id = [int(x) for x in attr["user_id"]][0]
    newUser.account_ids = [int(x) for x in attr["account_ids"]]

    return newUser