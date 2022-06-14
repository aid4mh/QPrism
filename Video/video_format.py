import os

def video_format(video_path):
    """
    Get the format of the video file

    This function returns a string which is the extension of the video file fed

    Parameters
    -----------
    video_path : path to the specific video

    Returns
    -------
    string
        '.mp4'
    """

    split_tup = os.path.splitext(video_path)
    format = (split_tup[-1])

    return format