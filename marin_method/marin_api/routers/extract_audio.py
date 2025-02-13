# ROUTERS
from fastapi import APIRouter
from marin_api.operations.extract_audio import extract_audio_from_one_video

router = APIRouter()

# POST
@router.post('/extract_audio/')
def api_download_video(data: dict):
    # dict = {url:video_url,encoder:mp3 or wav}
    return extract_audio_from_one_video(data)
