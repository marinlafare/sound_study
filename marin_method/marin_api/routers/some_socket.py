# ROUTERS

import random
from fastapi import APIRouter
# from main_api.operations.some_socket import some_socket_session

router = APIRouter()

@router.get("/some_socket/{user_name}")
def api_some_socket_session(user_name: str):
    return "some_socket_session(user_name)"
