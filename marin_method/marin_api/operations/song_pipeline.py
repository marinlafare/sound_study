# OPERATIONS
from marin_api.operations.download_video import download_video
from marin_api.operations.extract_audio import extract_audio_from_one_video
from marin_api.operations.separate_voice import separate_voice_from_one_audio

def song_pipeline(data):
    download_video(data)
    extract_audio_from_one_video(data)
    separate_voice_from_one_audio(data)
    return f"{data} ready"