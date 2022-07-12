import cv2


def video_resolution(video_path):
    """
    Get the resolution of the video file

    This function returns a string which is the resolution of the video file fed

    Parameters
    -----------
    video_path : path to the specific video

    Returns
    -------
    string
        '1680'
    """

    vid = cv2.VideoCapture(video_path)
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    resolution = int(height)
    return resolution
