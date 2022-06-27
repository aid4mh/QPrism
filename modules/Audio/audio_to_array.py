from scipy.io import wavfile
import sys
import numpy as np


def to_array(wav_path, print_full=False):
    """
    Convert an audio file to an array that can be used for plotting graphs and further audio exploration. It can be printed in full, but not recommended since it can be a very large array.

    This function takes the path of a wav audio file and returns the audio array

    Parameters
    -----------
    wav_path : path of a .wav audio
    print_full (Optional, default = False): If True, the full non-truncated representation of the array is printed

    Returns
    -------
    arr
        numpy array of the audio
        "[ 0  0  0 ...  8  0 -2]"
    """
    rate, data = wavfile.read(wav_path, 'rb')
    if print_full == True:
        np.set_printoptions(threshold=sys.maxsize)
    arr = np.array(data)
    return arr
