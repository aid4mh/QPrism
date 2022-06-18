import os

from pathlib import Path

# from modules.Audio.audio_classification import audio_classification
# from modules.Audio.audio_length import audio_length
# from modules.Audio.audio_paths import audio_paths
# from modules.Audio.audio_sample_rate import sample_rate
# from modules.Audio.audio_to_array import aud_to_array
from modules.Audio.extract_audios import extract_audios
# from modules.Audio.mp3_to_wav import mp3_to_wav
# from modules.Audio.noise_reduction import reduce_noise
# from modules.Audio.punctuator import punctuate
# from modules.Audio.speechtotext import audio_translate

from modules.Video.bit_rate import bitrate
from modules.Video.brightness import brightness
from modules.Video.creation_time import creation_time
from modules.Video.frame_rate import fps
from modules.Video.object_detection import detect_objects
from modules.Video.video_format import video_format
from modules.Video.video_length import video_length
from modules.Video.video_paths import video_paths
from modules.Video.video_resolution import video_resolution


class Video:

    def __init__(self):
        self.metrics = ['bitrate', 'brightness', 'creation_time', 'framerate',\
                        'video_format', 'video_length', 'video_resolution']


    def video_length(self, path:str):
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
                length[file] = video_length(file)
            
            return length

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
                resolution[file] = video_resolution(file)
            
            return resolution

        else:
            return video_resolution(path)

    
    def video_format(self, path:str):
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
                format[file] = video_format(file)
            
            return format

        else:
            return video_format(path)


    def bitrate(self, path:str):
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

            return bps

        else:
            video_name = str(Path(path).stem)
            audio_name = Path(video_name + "_Audio.mp3")
            audio_path = os.path.join(os.getcwd(), 'audio_files', audio_name)
            if not os.path.isfile(audio_path):
                print("Audio file not found!!!")
                print("Extracting audio from video")
                extract_audios(path)

            return bitrate(path, audio_path)


    def detect_objects(self, path:str, modelname:str):
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
                objects[file] = detect_objects(file, modelname)
            
            return objects

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
                framerate[file] = fps(file)
            
            return framerate

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
                b[file] = brightness(file)
            
            return b
        else:
            return brightness(path)