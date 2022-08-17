import csv
import os

import pandas as pd
from pathlib import Path

# Video functions
from QPrism.Video.bit_rate import bitrate
from QPrism.Video.brightness import video_brightness
from QPrism.Video.creation_time import creation_time
from QPrism.Video.frame_rate import fps
from QPrism.Video.object_detection import detect_objects, load_model
from QPrism.Video.video_format import video_format
from QPrism.Video.video_length import video_length
from QPrism.Video.video_resolution import video_resolution
from QPrism.Video.artifacts import noise_detection

# Helpers 
from QPrism.Video.helpers.extract_audios import extract_audios
from QPrism.Video.helpers.video_paths import video_paths


class Video_DQM:

    def __init__(self):
        self.vid_metrics = ['bitrate', 'brightness', 'creation_time', 'framerate',\
                        'video_format', 'video_length', 'video_resolution']


    def duration(self, path:str):
        """
        This function gives the length for both a folder of audios or a single audio file.

        Returns the length of the input audio if the input path is a file. 
        Returns a dict matching the input audio files to their length if the input path is a folder.

        Parameters
        ----------
            path : str
                A path to a folder or a file.

        """

        if os.path.isdir(path):
            video_files = video_paths(path)
            length = {}
            
            for file in video_files:
                length[str(Path(file).stem)] = video_length(file)
            
            return pd.DataFrame(length.items(), columns=['Videos', 'Length'])

        else:
            return video_length(path)


    def resolution(self, path:str):
        """
        This function returns the resolution of a video or the videos in given folder

        Parameters
        ----------
            path : str
                path to a folder or a file
        """

        if os.path.isdir(path):
            video_files = video_paths(path)
            resolution = {}
            
            for file in video_files:
                resolution[str(Path(file).stem)] = video_resolution(file)
            
            return pd.DataFrame(resolution.items(), columns=['Videos', 'Resolution'])

        else:
            return video_resolution(path)


    def format(self, path:str):
        """
        Get the format of the video
        This functions calls the video_format function and 
        gives the format for both a folder of videos or a single video file.

        Parameters
        ----------
        path : path to a folder or a file

        Returns
        -------
        dict (incase of folder)
        str (incase of file)
            dict : {'video_file1' : '.mp4', ... 'video_filen' : '.mp4'}
            str : '.mp4'
        """

        if os.path.isdir(path):
            video_files = video_paths(path)
            format = {}
            
            for file in video_files:
                format[str(Path(file).stem)] = video_format(file)
            
            return pd.DataFrame(format.items(), columns=['Videos', 'Format'])

        else:
            return video_format(path)


    def bit_rate(self, path:str):
        """
        Get the bit rate of the video
        
        Returns the bit rate for input video or each video in the input folder.

        Parameters
        ----------
            path : str
                path to a folder or a file
        """

        if os.path.isdir(path):
            video_files = video_paths(path)
            bps = {}
            for file in video_files:
                video_name = str(Path(file).stem)
                audio_name = Path(video_name + "_Audio.mp3")
                audio_path = os.path.join(os.getcwd(), 'audio_files', audio_name)
                if not os.path.isfile(audio_path):
                    print("Audio file not found!!!")
                    print("Extracting audio from video")
                    extract_audios(file)
                bps[video_name] = bitrate(file, audio_path)

            return pd.DataFrame(bps.items(), columns=['Videos', 'Bitrate'])

        else:
            video_name = str(Path(path).stem)
            audio_name = Path(video_name + "_Audio.mp3")
            audio_path = os.path.join(os.getcwd(), 'audio_files', audio_name)
            if not os.path.isfile(audio_path):
                print("Audio file not found!!!")
                print("Extracting audio from video")
                extract_audios(path)

            return bitrate(path, audio_path)


    def object_detection(self, path:str, modelname:str):
        """
        This function detect all the objects present in the video.

        Returns the detected objects in the video if the input path is a file.
        Returns a dict matching the input videos to their detected objects.

        Parameters
        ----------
            path : str
                path to a folder or a file
        """

        if os.path.isdir(path):
            model, classes = load_model(modelname)
            video_files = video_paths(path)
            objects = {}
            
            for file in video_files:
                objects[str(Path(file).stem)] = detect_objects(file, model, classes)
            
            return pd.DataFrame(objects.items(), columns=['Videos', 'Objects'])

        else:
            model, classes = load_model(modelname)
            return detect_objects(path, model, classes)


    def framerate(self, path:str):
        """
        This function get the framerate of the video.

        Returns the frame rate of the video if the input path is a file.
        Returns a dict matching the input videos to their frame rate if the input path is a folder.

        Parameters
        ----------
            path : str
                path to a folder or a file
        """

        if os.path.isdir(path):
            video_files = video_paths(path)
            framerate = {}
            
            for file in video_files:
                framerate[str(Path(file).stem)] = fps(file)
            
            return pd.DataFrame(framerate.items(), columns=['Videos', 'Framerate'])

        else:
            return fps(path)


    def illumination(self, path:str):
        """
        This function gives the brightness of the video.

        Returns the brightness of the video if the input path is a file.
        Returns a dict matching the input videos to their frame rate if the input path is a folder.

        Parameters 
        ----------
            path : str
                path to a folder or a file
        """

        if os.path.isdir(path):
            video_files = video_paths(path)
            b = {}
            
            for file in video_files:
                b[str(Path(file).stem)] = video_brightness(file)
            
            return pd.DataFrame(b.items(), columns=['Videos', 'Brightness'])
        else:
            return video_brightness(path)


    def creation_time(self, path:str):
        """
        This function gets the creation time of a video.

        Returns the creation time of the video if the input path is a file.
        Returns a dict matching the input videos to their creation time if the input path is a folder.

        Parameters
        -----------
            path : str
                path to a folder or a file
        """

        if os.path.isdir(path):
            video_files = video_paths(path)
            time = {}
            
            for file in video_files:
                time[str(Path(file).stem)] = creation_time(file)
            
            return pd.DataFrame(time.items(), columns=['Videos', 'Date created'])

        else:
            return creation_time(path)


    def artifacts_ratio(self, path:str):
        """
        This function gets how much of the video that contains video artifacts

        Returns the ratio of the video that contains artifacts (motion blur, too grainy, static) if the input path is a file.
        Returns a dict mathing the input videos to their artifacts percentage if the input path is a folder.

        Parameters
        -----------
            path : str
                path to a folder or a file
        """

        if os.path.isdir(path):
            video_files = video_paths(path)
            percents = {}
            
            for file in video_files:
                percents[str(Path(file).stem)] = noise_detection(file)
            
            return pd.DataFrame(percents.items(), columns=['Videos', 'Artifacts'])
        else:
            return noise_detection(path)


    def save_csv(self, path:str, output_path:str, modelname='yolov5s'):
        """
        Creates a csv file consists of all the video metrics.

        Saves a csv file to the input path with all video quality metrics 

        Parameters
        ----------
            path : str
                path to single video file or folder
            output_path : str
                path to the output csv file
            modelname : str
                yolov5 model name for object detection
        """

        if os.path.isdir(path):
            video_files = video_paths(path)
        else:
            video_files = [os.path.abspath(path)]

        with open('video_metrics.csv', 'w') as file:
            header = ['Video Name', 'Bit Rate', 'Illumination', 'Date of Creation', 'Frame Rate', \
                        'Format', 'Duration', 'Resolution', 'Object Detection', 'Artifacts Ratio']
            writer = csv.writer(file)
            writer.writerow(header)

        csv_path = output_path
        metrics = pd.DataFrame()

        for i, video in enumerate(video_files):
            data_row = []

            data_row.append(str(Path(video).stem))
            data_row.append(self.bit_rate(video))
            data_row.append(self.illumination(video))
            data_row.append(self.creation_time(video))
            data_row.append(self.framerate(video))
            data_row.append(self.format(video))
            data_row.append(self.duration(video))
            data_row.append(self.resolution(video))
            data_row.append(self.object_detection(video, modelname))
            data_row.append(self.artifacts_ratio(video))

            data_series = pd.Series(data_row, index=header)
            metrics = metrics.append(data_series, ignore_index=True)
        
        print('Metrics saved to ', csv_path)
        metrics.to_csv(csv_path, index=False)