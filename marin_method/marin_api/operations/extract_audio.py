#OPERATONS
from pytubefix import YouTube
from raw_data.raw_data import videos_waiting_for_extract, audio_dir

def get_file_name_from_video_url(url):
    video_info = YouTube(url, use_oauth=True,
                 allow_oauth_cache=True)
    video_stream = video_info.streams.get_audio_only()
    title = video_stream.title.replace(" ","_")\
                        .replace("|","").replace('"',"").replace("?","")\
                        .replace("!","").replace('¿',"")
    return title

def extract_audio_from_one_video(data)->None:
    import ffmpeg
    from pytubefix import YouTube    
    url = data["url"]
    encoder = "mp3" or data["encoder"]
    title = get_file_name_from_video_url(url)  
    dirs = videos_waiting_for_extract()
    for song_dir in dirs:
        print("song_dir:",song_dir)
        print("title:",title)
        if title in song_dir:
            stream = ffmpeg.input(song_dir)
            stream = ffmpeg.output(stream, audio_dir + f"/{title}.{encoder}")
            ffmpeg.run(stream)
            return audio_dir + f"/{title}.{encoder} ready"