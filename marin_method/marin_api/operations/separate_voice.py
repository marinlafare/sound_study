# OPERATIONS
import os
from pytubefix import YouTube

audio_folder = "raw_data/raw_audio"
voices_folder = "raw_data/voices"

def get_file_name_from_video_url(url):
    video_info = YouTube(url, use_oauth=True,
                 allow_oauth_cache=True)
    video_stream = video_info.streams.get_audio_only()
    title = video_stream.title.replace(" ","_")\
                        .replace("|","").replace('"',"").replace("?","")\
                        .replace("!","").replace('¿',"")
    return title

def separate_voice_from_one_audio(data):
    from spleeter.separator import Separator
    
    url = data["url"]
    encoder =  "wav" or data["encoder"]
    title = get_file_name_from_video_url(url)
    song = [x for x in os.listdir(audio_folder) if title in x][0]
    separator = Separator(f"spleeter:2stems")
    separator.separate_to_file(os.path.join(audio_folder, song),
                            voices_folder,
                            duration = 540,
                            codec='wav',
                            filename_format='{filename}/{instrument}.{codec}')
    return f"SONG SEPARATED SUCCESFULLY: {title}"
