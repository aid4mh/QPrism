import os

from moviepy.editor import *


def bitrate(video_path, audio_path):
    """
    Get the bitrate of the video file

    This function returns the bit rate of the video file

    Parameters
    -----------
    video_path : path to the specific video
    audio_path : path to the specific audio

    Returns
    -------
    int
        1240
    """

    video = VideoFileClip(video_path)
    mp3_size = os.path.getsize(audio_path)
    vid_size = os.path.getsize(video_path)
    duration = video.duration
    bit_rate = int((((vid_size - mp3_size)/duration)/1024*8))

    return bit_rate