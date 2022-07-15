import math

import cv2

from PIL import Image, ImageStat


def brightness_frame(im):
    """
    Get the brightness of the video frame

    This function returns the brightness of the video frame

    Parameters
    -----------
    im : frame of the video in the form of an image

    Returns
    -------
    float
        28.32078
    """

    im = Image.fromarray(im)
    stat = ImageStat.Stat(im)
    r,g,b = stat.mean

    return math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))


def video_brightness(video_file):
    """
    Get the average brightness of the video file

    This function returns the average brightness of the frames of a video file

    Parameters
    -----------
    video_file : path to a specific video 

    Returns
    -------
    float
        125.7859249810
    """

    cap = cv2.VideoCapture(video_file)
    bright = list()
    while(True):
        ret, frame = cap.read()
        if ret: 
            bright.append(brightness_frame(frame))
        else:
            return round(sum(bright)/len(bright), 3) if len(bright) > 0 else 0
