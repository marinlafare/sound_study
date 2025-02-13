# OPERATIONS
import os
from pytubefix import YouTube

def download_video(data):
    video_info = YouTube(data["url"], use_oauth=True,
                 allow_oauth_cache=True)
    video_stream = video_info.streams.get_audio_only()
    title = video_stream.title.replace(" ","_")\
                        .replace("|","").replace('"',"").replace("?","")\
                        .replace("!","").replace('¿',"")
    if os.path.exists(f"raw_data/raw_video/{title}"):
        return f"video for ::: {title} ready"
    else:
        video_stream.download(f"raw_data/raw_video/{title}")
        return f"video for ::: {title} ready"