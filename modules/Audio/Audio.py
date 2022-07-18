import csv
import os

import pandas as pd
from pathlib import Path

# Audio functions
from modules.Audio.audio_classification import audio_classification
from modules.Audio.audio_length import audio_length
from modules.Audio.audio_sample_rate import sample_rate
from modules.Audio.noise_reduction import reduce_noise

# Helpers 
from modules.Audio.helpers.audio_to_array import aud_to_array
from modules.Audio.helpers.audio_paths import audio_paths
from modules.Audio.helpers.to_mono_wav import to_mono_wav


class Audio:
    def __init__(self):
        self.aud_metrics = ['classification', 'audio_length', 'sample_rate', 'aud_to_array',\
                            'mp3_to_wav', 'noise_reduction', 'audio_translation']


    def mp3_to_wav(self, path:str):
        """
        Convert mp3 files to mono wav files

        This function takes in mp3 audio files and converts them into mono wav files to be used for deep learning and further exploration.

        Parameters
        -----------
        mp3_path : path to the .mp3 file

        Returns
        -------
        NONE
            Saves the .wav file in the same working directory
            "audio_Wav.wav"
        """

        # if os.path.isdir(path):
        #     audio_files = audio_paths(path)

        #     for file in audio_files:
        #         mp3_wav(file)
        
        # else:
        #     mp3_wav(path)


    def audio_length(self, path:str):
        """
        Get the length of the audio
        
        This functions calls the audio_length function and 
        gives the length for both a folder of audios or a single audio file.

        Parameters
        ----------
        path : path to a folder or a file

        Returns
        -------
        dict (incase of folder)
        int (incase of file)
            dict : {'audio_file1' : 101, ... 'audio_filen' : 89}
            int : 101
        """

        if os.path.isdir(path):
            audio_files = audio_paths(path)
            length = {}
            
            for file in audio_files:
                length[file] = audio_length(file)
            
            return length

        else:
            return audio_length(path)

    
    def sample_rate(self, path:str):
        """
        Get the sample rate of the audio
        
        This functions calls the sample_rate function and 
        gives the bit rate for both a folder of audios or a single audio file.

        Parameters
        ----------
        path : path to a folder or a file

        Returns
        -------
        dict (incase of folder)
        int (incase of file)
            dict : {'audio_file1' : 1024, ... 'audio_filen' : 1399}
            int : 1024
        """

        if os.path.isdir(path):
            audio_files = audio_paths(path)
            s_rate = {}

            for file in audio_files:
                s_rate[file] = sample_rate(file)
            
            return s_rate

        else:
            return sample_rate(path)


    def audio_2_array(self, path:str):
        """
        Reads audio file and transforms it into numpy array

        Parameters
        ----------
        audio_path : path to the the audio file

        Returns
        -------
        dict --> (incase of folder)
        tuple(int, Numpy array) --> (incase of file)
        """
        if os.path.isdir(path):
            audio_files = audio_paths(path)
            array = {}

            for file in audio_files:
                array[file] = aud_to_array(file)
            
            return array

        else:
            return aud_to_array(path)

    
    def audio_translation(self, path:str):
        """
        This function translate the given audio file into punctuated text using the Google API

        Parameters
        ----------
        path : name of the audio_file / audio_folder

        Returns
        -------
        string, float
                "some text ", 0.6754368
        """ 
        p = Punctuator('Demo-Europarl-EN.pcl')

        if os.path.isdir(path):
            audio_files = audio_paths(path)
            data = {}

            for file in audio_files:
                data[file] = {}
                text, conf = audio_translate(file)

                data[file]['Confidence'] = conf
                data[file]['Text'] = p.punctuate(text)
            
            return data

        else:
            text, conf = audio_translate(path)
            return p.punctuate(text), conf

    
    def audio_classify(self, path:str):
        """
        Get a list of all the sounds in an audio

        This function returns a list of all the prominent sounds inside the audio

        Parameters
        ----------
        path : path to a folder or a file

        Returns
        -------
        dict (incase of folder)
        list (incase of file)
            dict : {'audio_file1' : ['Speech', 'Whistling', 'Alarm'], ... 'audio_filen' : 'Speech', 'Alarm']}
            list : ['Speech', 'Whistling', 'Alarm']
        """
        if os.path.isdir(path):
            audio_files = audio_paths(path)
            sounds = {}

            for file in audio_files:
                sounds[file] = audio_classification(file)
            
            return sounds
        
        else:
            return audio_classification(path)

    
    def noise_reduce(self, path:str):
        """
        Remove the background noise of an audio

        This function takes the path of a wav audio file and saves a new one with no background noise using non-stationary noise reduction

        Parameters
        -----------
        wav_path : path of a .wav audio

        Returns
        -------
        NONE
            saves the cleaned .wav audio in the working directory
            "example_cleaned.wav"
        """
        if os.path.isdir(path):
            audio_files = audio_paths(path)

            for file in audio_files:
                reduce_noise(file)
        
        else:
            reduce_noise(path)