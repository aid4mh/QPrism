import numpy as np
from numpy.fft import fft, fftfreq
import matplotlib.pyplot as plt
from scipy.io import wavfile
import math
import matplotlib.pyplot as plt
import pandas as pd

def snr(wav_path, plot_env=False, plot_noise=False):
    data = wavfile.read(wav_path)[1]
    window_size = 3
    numbers_series = pd.Series(data)
    windows = numbers_series.rolling(window_size)
    moving_averages = windows.mean()
    moving_averages_list = moving_averages.tolist()
    new_data = moving_averages_list[window_size - 1:]
    max_power = np.max(np.abs(new_data)**2)
    threshold = 0.10 * math.sqrt(max_power)
    def getEnvelope (inputSignal):
       
        absoluteSignal = []
        for sample in inputSignal:
            absoluteSignal.append (abs (sample))

        intervalLength = 250
        outputSignal = []
        
        for baseIndex in range (intervalLength, len (absoluteSignal)):
            maximum = 0
            for lookbackIndex in range (intervalLength):
                maximum = max (absoluteSignal [baseIndex - lookbackIndex], maximum)
            outputSignal.append (maximum)
        return outputSignal
    env = getEnvelope(new_data)
    if plot_env == True:
        plt.plot(new_data)
        plt.plot(env)
        plt.title("Signal with envelope highlighted")
        plt.show()
    mask = np.array([0 if i > threshold else 1 for i in new_data])
    noise = new_data * mask
    noise = noise[noise != 0]
    data_fft = fft(new_data)
    noise_fft = fft(noise, n=len(data_fft))
    true_data = data_fft - noise_fft
    power_signal = np.abs(true_data)**2
    power_noise = np.abs(noise_fft)**2
    if plot_noise == True:
        noisysig_power = np.abs(data_fft)**2
        noisysig_freq = fftfreq(len(noisysig_power))
        noise_freq = fftfreq(len(power_noise))
        plt.figurefigsize = (8, 4)
        plt.plot(noisysig_freq[noisysig_freq>0], 10*np.log10(noisysig_power[noisysig_freq>0]));
        plt.plot(noise_freq[noise_freq>0], 10*np.log10(power_noise[noise_freq>0]));
        plt.show()

    snr = 10*np.log10(np.sum(power_signal) / np.sum(power_noise))
    return snr

    