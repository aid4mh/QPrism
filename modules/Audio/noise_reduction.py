from scipy.io import wavfile
import noisereduce as nr
import numpy as np
from pathlib import Path
from scipy.io.wavfile import write


def reduce_noise(wav_path):
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
    rate, data = wavfile.read(wav_path, 'rb')
    reduced_noise = nr.reduce_noise(
        y=data, sr=rate, thresh_n_mult_nonstationary=2, stationary=False)
    audio_name = str(Path(wav_path).stem)
    cleaned_name = Path(audio_name + "_cleaned.wav")
    absmax = np.max(np.abs(reduced_noise))
    data32 = (reduced_noise/absmax).astype(np.float32)
    write(cleaned_name, int(rate), data32)
