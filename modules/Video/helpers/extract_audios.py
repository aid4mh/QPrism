import os
from genericpath import exists
from pathlib import Path
from moviepy.editor import *

def extract_audios(video_path):
    """
    Extract the audio of the video file

    This function extracts the audio of the video file fed and saves in the audio directory

    Parameters
    -----------
    video_path : path to the specific video

    Returns
    -------
    Audio filename (string) 
        'user_1696_video_diary_867227_Audio.mp3'
    """

    video_name = str(Path(video_path).stem)
    audio_dir = 'audio_files'
    os.makedirs(audio_dir, exist_ok=True)
    audio_name = Path(video_name + "_Audio.mp3")

    try:
        if not audio_name.exists():
            videoclip = VideoFileClip(video_path)
            audioclip = videoclip.audio
            audioclip.write_audiofile(os.path.join(audio_dir, audio_name))
            audioclip.close()
            videoclip.close()
        else:
            pass
        return audio_name

    except OSError:
        print('Encountered OSError')
        return None

