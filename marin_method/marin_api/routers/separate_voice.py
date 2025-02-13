# ROUTERS
from fastapi import APIRouter
from marin_api.operations.separate_voice import separate_voice_from_one_audio
router = APIRouter()

# POST
@router.post('/separate_voice/')
def api_download_video(data: dict):
    # dict = {url:video_url,encoder:mp3 or wav}
    return separate_voice_from_one_audio(data)
