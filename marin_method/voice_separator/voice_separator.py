import os
import ffmpeg
import string
# from main_api.operations.constants import *

def separate_voice(audio_file, stems = 2):
    from spleeter.separator import Separator
    import librosa
    separator = Separator(f"spleeter:{stems}stems")
    separator.separate_to_file(os.path.join(AUDIOS_FOLDER, audio_file),
                            RESULTS_FOLDER,
                            duration = 540,
                            codec='wav',
                            filename_format='{filename}/{instrument}.{codec}')
    return f"SONG SEPARATED SUCCESFULLY: {audio_file}"
    # return f"CORRECT FUNCTION {audio_file}"
def popo():
    return "POPO WORKS"
if __name__ == "__main__":
    song_name = input(" song_file name please: ")
    song = os.path.join(AUDIOS_FOLDER,song_name)
    separate_voice(song, stems = 2)