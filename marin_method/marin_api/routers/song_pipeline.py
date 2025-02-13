# ROUTERS
from fastapi import APIRouter
from marin_api.operations.song_pipeline import song_pipeline
router = APIRouter()

# POST
@router.post('/song_pipeline/')
def api_download_video(data: dict):
    # dict = {url:video_url,encoder:mp3 or wav}
    return song_pipeline(data)
