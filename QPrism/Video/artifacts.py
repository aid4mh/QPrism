import cv2
import numpy as np


def noise_detection(video_path):
    """
      Get how much of the video that contains video artifacts

      This function returns the ratio of the video that contains artifacts (motion blur, too grainy, static)

      Parameters
      -----------
      video_path : path to a video

      Returns
      -------
      float
          0.284
    """
    cap = cv2.VideoCapture(video_path)
    vid_noise = []
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        s = cv2.calcHist([image], [1], None, [256], [0, 256])
        p = 0.05
        s_perc = np.sum(s[int(p * 255):-1]) / np.prod(image.shape[0:2])
        s_thr = 0.5
        if s_perc > s_thr:
            vid_noise.append(1)
        else:
            vid_noise.append(0)
    return round((sum(vid_noise)/len(vid_noise)), 3)
