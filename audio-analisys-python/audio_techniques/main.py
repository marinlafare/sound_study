# MAIN
import os
import fastapi
from fastapi import FastAPI, WebSocket,WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from bfi_api.routers import countries, auto_test, about_kaggle_data, admin
from bfi_api.operations.auto_test import init_auto_test, init_llm_test
from bfi_api.operations.connection import Connection, create_json
from bfi_api.data.engine import init_db
from bfi_api.data.models import Subject

app = FastAPI()
origins = ["http://127.0.0.1:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(countries.router)
app.include_router(auto_test.router)
app.include_router(about_kaggle_data.router)
app.include_router(admin.router)


connection = Connection()


@app.on_event("startup")
def startup_event():
    init_db()
    print('#########    new_bfi_server_started    #########')
@app.get('/')
def read_root():
    return 'PYTHON_API ** BFI SERVER RUNNING **'

@app.websocket("/ws/{lang}/{n_questions}/{count_id}")
def api_auto_test(websocket: WebSocket,
                    lang:str,
                    n_questions:str,
                    count_id: str):    
    print(f'## main.py_@app.websocket("/ws/{lang}/{n_questions}/{count_id}") \n ##')
    return init_auto_test(websocket,
                            lang,
                            n_questions,
                            count_id)
@app.websocket("/ws/llm/{lang}/{n_questions}/{user_name}/{count_id}")
def api_auto_llm_test(websocket: WebSocket,
                    lang:str,
                    n_questions:str,
                    user_name:str,
                    count_id: str):
    # restringe the pass to just numbers
    # if user_id in ["11","22","33"]:
    # uvicorn main:app --reload --ws-ping-timeout 200
    print("##")
    print(f'LLM\nmain.py_@app.websocket("/ws/llm/{lang}/{n_questions}/{count_id}")')
    print("##")
    
    return init_llm_test(websocket,
                            lang,
                            n_questions,
                            user_name,
                            count_id)
# ##
# def lang_info(lang):
#     return f" The user only speaks {lang}, so you have to read and to respond in {lang}"