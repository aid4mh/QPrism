import cv2
import torch


def load_model(modelname):
    """
    Loads the object detection model from the torch hub
    Parameters
    ----------
    None
    Returns
    -------
    callable, list
        model, ['person', 'bicycle', ... 'hair brush']
    """

    model = torch.hub.load('ultralytics/yolov5',
                            modelname)
    classes = model.names
    
    return model, classes


def detect_objects(video_file, model, classes):
    """
    Get the objects present in the video

    This function returns the a set of objects found in the video file

    Parameters
    -----------
    video_file : path to a specific video 
    model : CNN model used for object detection
    classes: labels of the coco dataset

    Returns
    -------
    set
        {'person', 'cell phone', 'chair', 'tv'}
    """

    # model, classes = load_model(modelname)

    cap = cv2.VideoCapture(video_file)
    objects = list()
    while True:
        ret, frame = cap.read()
        if ret:
            result = model(frame)
            result.show()
            labels = result.xyxyn[0][:, -1].cpu().numpy()
            for index in range(len(labels)):
                objects.append(classes[int(labels[index])])
        else:
            return list(set(objects))
            