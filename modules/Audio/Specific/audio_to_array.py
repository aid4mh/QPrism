from mutagen.mp3 import MP3
import pydub
import numpy as np


def aud_to_array(audio_path, normalized=False):
    """
    Reads audio file and transforms it into numpy array

    Parameters
    ----------
    audio_path : path to the the audio file

    Returns
    -------
    Numpy array
    """
    audio = pydub.AudioSegment.from_mp3(audio_path)
    samples = np.array(audio.get_array_of_samples())
    if audio.channels == 2:
        samples = samples.reshape((-1, 2))
    if normalized:
        return audio.frame_rate, np.float32(samples) / 2**15
    else:
        return audio.frame_rate, samples
