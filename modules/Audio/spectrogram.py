import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import numpy as np


def aud_spectrogram(wav_path, log=False):
    """
    A spectrogram is a figure which represents the spectrum of frequencies of a recorded audio over time. 

    This function returns the spectrogram of the audio with the option of a logarithmic scale.

    Parameters
    -----------
    wav_path: path to a .wav audio
    log (Optional, Default=False): If true, displays the spectrogram with a logarithmic scale.

    Returns
    -------
    Graph: displays the spectrogram 

    """
    sample_rate, samples = wavfile.read(wav_path)
    frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)
    plt.pcolormesh(np.log(spectrogram))
    plt.ylabel('Frequency [Hz]')
    if log == True:
        plt.yscale('symlog')
    plt.xlabel('Time [sec]')
    plt.show()
