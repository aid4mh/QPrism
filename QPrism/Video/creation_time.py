import ast
import os
import subprocess


def creation_time(video_path):
    """
    Get the creation time of a video

    This function returns the date of when the video was created

    Parameters
    -----------
    video_path : path to a specific video 

    Returns
    -------
    string
        "2022-05-29 23:22:59.599607"

    """
    byteD = subprocess.check_output(['ffprobe', '-v', 'quiet', video_path, '-print_format',
                                     'json', '-show_entries', 'stream=index,codec_type:stream_tags=creation_time:format_tags=creation_time'])
    dict = byteD.decode("UTF-8")
    mydata = ast.literal_eval(dict)
    try:
        time = mydata['format']['tags']['creation_time']
    except(KeyError):
        time = 'N/A'
    return str(time).split('.')[0]
