# ROUTERS
from fastapi import APIRouter
from marin_api.operations.download_video import download_video
router = APIRouter()

# POST
@router.post('/download_video/')
def api_download_video(data: dict):
    return download_video(data)
