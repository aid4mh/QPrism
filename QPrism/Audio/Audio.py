import csv
import os

import pandas as pd
from pathlib import Path

# Audio functions
from QPrism.Audio.audio_classification import audio_classification
from QPrism.Audio.audio_length import audio_length
from QPrism.Audio.audio_sample_rate import sample_rate
from QPrism.Audio.audio_rms import rms
from QPrism.Audio.snr import snr

# Helpers
from QPrism.Audio.helpers.audio_to_array import to_array
from QPrism.Audio.helpers.audio_paths import audio_paths
from QPrism.Audio.helpers.to_mono_wav import to_mono_wav


class Audio:
    def __init__(self):
        self.aud_metrics = ['classification', 'audio_length', 'sample_rate', 'rms'
                            'signal_to_noise']

    def length(self, path: str):
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
                if not file.startswith('.'):
                    length[str(Path(file).stem)] = audio_length(file)

            return pd.DataFrame(length.items(), columns=['Audios', 'Length'])

        else:
            return audio_length(path)

    def sample_rate(self, path: str):
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
                if not file.startswith('.'):
                    s_rate[str(Path(file).stem)] = sample_rate(file)

            return pd.DataFrame(s_rate.items(), columns=['Audios', 'Sample Rate'])

        else:
            return sample_rate(path)

    def audio_classify(self, path: str):
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
                if not file.startswith('.'):
                    sounds[str(Path(file).stem)] = audio_classification(file)

            return pd.DataFrame(sounds.items(), columns=['Audios', 'Voices'])

        else:
            return audio_classification(path)

    def root_mean_square(self, path: str):
        """
        RMS level (root mean squared) is just proportional to the amount of energy over a period of time in the signal. This can be used to distinguish audios that are louder from each other.
        This function returns the rms value of a given function.

        Parameters
        -----------
        wav_path : path to a .wav audio

        Returns
        -------
        int: the rms value of the audio
            "880"
        """

        if os.path.isdir(path):
            audio_files = audio_paths(path)
            rms_values = {}

            for file in audio_files:
                if not file.startswith('.'):
                    rms_values[str(Path(file).stem)] = rms(file)

            return pd.DataFrame(rms_values.items(), columns=['Audios', 'RMS'])

        else:
            return rms(path)

    def signaltonoise(self, path: str):
        """
        RMS level (root mean squared) is just proportional to the amount of energy over a period of time in the signal. This can be used to distinguish audios that are louder from each other.
        This function returns the rms value of a given function.

        Parameters
        -----------
        wav_path : path to a .wav audio

        Returns
        -------
        int: the rms value of the audio
            "880"
        """

        if os.path.isdir(path):
            audio_files = audio_paths(path)
            snr_values = {}

            for file in audio_files:
                if not file.startswith('.'):
                    snr_values[str(Path(file).stem)] = round(snr(file), 3)

            return pd.DataFrame(snr_values.items(), columns=['Audios', 'SNR'])

        else:
            return round(snr(path), 3)

    def all_audio(self, path: str):
        """
        Creates a csv file with all the audio metrics

        Parameters:
        ----------
        path: path to single audio file or folder

        Returns
        -------
        Writes a csv file to the path "audio_metrics.csv"
        """

        if os.path.isdir(path):
            audio_files = audio_paths(path)
        else:
            audio_files = [os.path.abspath(path)]

        with open('audio_metrics.csv', 'w') as file:
            header = ['Audio Name', 'Length',
                      'Sample Rate', 'Voices', 'SNR', 'RMS']
            writer = csv.writer(file)
            writer.writerow(header)

        csv_path = str(os.getcwd()) + '/audio_metrics.csv'
        metrics = pd.read_csv(csv_path)

        for i, audio in enumerate(audio_files):
            data_row = []

            data_row.append(str(Path(audio).stem))
            data_row.append(self.length(audio))
            data_row.append(self.sample_rate(audio))
            data_row.append(self.audio_classify(audio))
            data_row.append(self.signaltonoise(audio))
            data_row.append(self.root_mean_square(audio))

            data_series = pd.Series(data_row, index=metrics.columns)
            metrics = metrics.append(data_series, ignore_index=True)

        print('Metrics saved to ', csv_path)
        metrics.to_csv(csv_path, index=False)
