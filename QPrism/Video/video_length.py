import cv2 

from QPrism.Video.frame_rate import fps


def video_length(video_path):
    """
    Get the length of the video file

    This function returns the video length (seconds) of the video file

    Parameters
    -----------
    video_path : path to the specific video

    Returns
    -------
    int
        101
    """

    video_data = cv2.VideoCapture(video_path)
    frames = video_data.get(cv2.CAP_PROP_FRAME_COUNT)
    video_length = int(frames / fps(video_path))
    return video_length