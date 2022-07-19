from scipy.io import wavfile
import numpy as np
import pandas as pd
import wave
from pathlib import Path


def to_timeseries_dataframe(wav_path, save=False):
    """
    Get the timeseries data frame of an audio

    This function returns a .csv data frame containing the time stamps and data of each channel in each column

    Parameters
    -----------
    wav_path : path to a .wav audio
    save (optional, default=False): If True saves the data frame as a csv file in the working directory.

    Returns
    -------
    Data Frame: contains the time stamps in the first column and channels with corresponding data in the remaining columns. File is saved in working dorectory.
    """
    raw = wave.open(wav_path)
    nch = raw.getnchannels()
    samplerate, data = wavfile.read(wav_path)
    data_per_channel = [data[offset::nch] for offset in range(nch)]
    duration = data.shape[0]/samplerate
    time = np.arange(0, duration, 1/samplerate)
    aud_data = {'Time': time}
    for i in range(0, nch):
        ch_name = 'Channel_' + str(i+1)
        ch_arr = np.ravel(data_per_channel[i])
        aud_data[ch_name] = np.resize(ch_arr, data.shape[0])
    audio_data = pd.DataFrame(aud_data)
    if save == True:
        audio_name = str(Path(wav_path).stem)
        audio_data.to_csv(audio_name+'.csv')
    return audio_data
