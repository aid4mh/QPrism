import csv
import os

import pandas as pd
from pathlib import Path

# Video functions
from modules.Video.bit_rate import bitrate
from modules.Video.brightness import video_brightness
from modules.Video.creation_time import creation_time
from modules.Video.frame_rate import fps
from modules.Video.object_detection import detect_objects
from modules.Video.video_format import video_format
from modules.Video.video_length import video_length
from modules.Video.video_resolution import video_resolution
from modules.Video.artifacts import noise_detection

# Helpers 
from modules.Video.helpers.extract_audios import extract_audios
from modules.Video.helpers.video_paths import video_paths


class Video:

    def __init__(self):
        self.vid_metrics = ['bitrate', 'brightness', 'creation_time', 'framerate',\
                        'video_format', 'video_length', 'video_resolution']


    def length(self, path:str):
        """
        Get the length of the video
        This functions calls the video_length function and 
        gives the length for both a folder of videos or a single video file.

        Parameters
        ----------
        path : path to a folder or a file

        Returns
        -------
        dict (incase of folder)
        int (incase of file)
            dict : {'video_file1' : 101, ... 'video_filen' : 89}
            int : 101
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
        Get the resolution of the video
        This functions calls the video_resolution function and 
        gives the resolution for both a folder of videos or a single video file.

        Parameters
        ----------
        path : path to a folder or a file

        Returns
        -------
        dict (incase of folder)
        str (incase of file)
            dict : {'video_file1' : '1280 x 820', ... 'video_filen' : '640 X 640'}
            str : '1280 x 820'
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
        This functions calls the bit_rate function and 
        gives the bit rate for both a folder of videos or a single video file.

        Parameters
        ----------
        path : path to a folder or a file

        Returns
        -------
        dict (incase of folder)
        int (incase of file)
            dict : {'video_file1' : 1024, ... 'video_filen' : 1399}
            int : 1024
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
        Get the objects present in the video
        This functions calls the detect_objects function and gives the objects present in the video.

        Parameters
        ----------
        path : path to a folder or a file

        Returns
        -------
        nested dict (incase of folder)
        dict (incase of file)
            nested dict : {'video_file1' : {'person', 'dog', 'tie'}, ... 'video_filen' : {'person', 'dog'}}
            dict : {'person', 'dog', 'tie'}
        """

        if os.path.isdir(path):
            video_files = video_paths(path)
            objects = {}
            
            for file in video_files:
                objects[str(Path(file).stem)] = detect_objects(file, modelname)
            
            return pd.DataFrame(objects.items(), columns=['Videos', 'Objects'])

        else:
            return detect_objects(path, modelname)


    def framerate(self, path:str):
        """
        Get the framerate of the video
        This functions calls the fps function and 
        gives the frame rate for both a folder of videos or a single video file.

        Parameters
        ----------
        path : path to a folder or a file

        Returns
        -------
        dict (incase of folder)
        int (incase of file)
            dict : {'video_file1' : 29, ... 'video_filen' : 37}
            str : 29
        """

        if os.path.isdir(path):
            video_files = video_paths(path)
            framerate = {}
            
            for file in video_files:
                framerate[str(Path(file).stem)] = fps(file)
            
            return pd.DataFrame(framerate.items(), columns=['Videos', 'Framerate'])

        else:
            return fps(path)


    def brightness(self, path:str):
        """
        This function gives the brightness of a single video file or a folder containing the videos

        Parameters 
        ----------
        path : path to a specific video or a folder containing videos

        Returns
        -------
        dict : if folder is passed
        float : if single filepath is passed
            dict : {'video_file1' : 28.5985, ... 'video_filen' : 68.5673}
            float : 34.6783
        """

        if os.path.isdir(path):
            video_files = video_paths(path)
            b = {}
            
            for file in video_files:
                b[str(Path(file).stem)] = video_brightness(file)
            
            return pd.DataFrame(b.items(), columns=['Videos', 'Brightness'])
        else:
            return video_brightness(path)


    def time_created(self, path:str):
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

        if os.path.isdir(path):
            video_files = video_paths(path)
            time = {}
            
            for file in video_files:
                time[str(Path(file).stem)] = creation_time(file)
            
            return pd.DataFrame(time.items(), columns=['Videos', 'Date created'])

        else:
            return creation_time(path)


    def check_artifacts(self, path:str):
        """
        Get how much of the video that contains video artifacts

        This function returns the percentage of the video that contains artifacts (motion blur, too grainy, static)

        Parameters
        -----------
        video_path : path to a video

        Returns
        -------
        float
            3.351
        """

        if os.path.isdir(path):
            video_files = video_paths(path)
            percents = {}
            
            for file in video_files:
                percents[str(Path(file).stem)] = noise_detection(file)
            
            return pd.DataFrame(percents.items(), columns=['Videos', 'Artifacts'])
        else:
            return noise_detection(path)


    def all_video(self, path:str, modelname:str):
        """
        Creates a csv file with all the video metrics

        Parameters:
        ----------
        path: path to single video file or folder
        modelname: yolov5 model name for object detection

        Returns
        -------
        Writes a csv file to the path "video_metrics.csv"
        """

        if os.path.isdir(path):
            video_files = video_paths(path)
        else:
            video_files = [os.path.abspath(path)]

        with open('video_metrics.csv', 'w') as file:
            header = ['Video Name', 'Bit Rate', 'Brightness', 'Date of Creation', 'Frame Rate', \
                        'Format', 'Length', 'Resolution', 'Objects', 'Artifacts']
            writer = csv.writer(file)
            writer.writerow(header)

        csv_path = str(os.getcwd()) + '/video_metrics.csv'  
        metrics = pd.read_csv(csv_path)

        for i, video in enumerate(video_files):
            data_row = []

            data_row.append(str(Path(video).stem))
            data_row.append(self.bit_rate(video))
            data_row.append(self.brightness(video))
            data_row.append(self.time_created(video))
            data_row.append(self.framerate(video))
            data_row.append(self.format(video))
            data_row.append(self.length(video))
            data_row.append(self.resolution(video))
            data_row.append(self.object_detection(video, modelname))
            data_row.append(self.check_artifacts(video))

            data_series = pd.Series(data_row, index=metrics.columns)
            metrics = metrics.append(data_series, ignore_index=True)
        
        print('Metrics saved to ', csv_path)
        metrics.to_csv(csv_path, index=False)