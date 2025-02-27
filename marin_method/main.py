# MAIN
import os
import fastapi
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from marin_api.operations.some_socket import some_socket_session
from marin_api.routers import download_video, extract_audio, separate_voice, song_pipeline
from marin_api.operations.connection import Connection
from marin_api.data.engine import init_db

app = FastAPI()
origins = ["http://127.0.0.1:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(download_video.router)
app.include_router(extract_audio.router)
app.include_router(separate_voice.router)
app.include_router(song_pipeline.router)


connection = Connection()


@app.on_event("startup")
def startup_event():
    init_db()
    print("#########    marin_method server it's ON YO!    #########")
@app.get('/')
def read_root():
    return '** marin_method server ** SERVER RUNNING **'
    
{"url":"https://www.youtube.com/watch?v=VMMAmNte-b4"}
@app.websocket("/ws/{user_name}")
def api_some_socket_session(websocket: WebSocket,
                             user_name:str):
    print("##")
    print(f'/ws/some_socket')
    print('socket')
    print("##")
    
    return some_socket_session(websocket,
                                 user_name,
                                 )