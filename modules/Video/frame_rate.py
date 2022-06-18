import cv2


def fps(video_path):
    """
    Get the frame rate of the video file

    This function returns the frame rate (fps) of the video file

    Parameters
    -----------
    video_path : path to the specific video

    Returns
    -------
    int
        29
    """

    video_data = cv2.VideoCapture(video_path)
    fps_vid = int(video_data.get(cv2.CAP_PROP_FPS))
    return fps_vid