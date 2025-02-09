from pytubefix import YouTube

def download_audio_from_youtube_video(url):
    yt = YouTube(url, use_oauth=True,
                 allow_oauth_cache=True)
    ys = yt.streams.get_audio_only()
    title = ys.title.replace(" ","_").replace("|","")
    
    ys.download(f"raw_data/raw_audio/{title}")