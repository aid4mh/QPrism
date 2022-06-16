from mutagen.mp3 import MP3
import pydub
import numpy as np


def array_to_audio(audio_name, frame_rate, samples, normalized=False):
    """
    transforms numpy array to audio

    Parameters
    ----------
    audio_name: the name of the output audio ex. "out.mp3"
    frame_rate: the frame rate of the audio
    samples: the numpy array of the audio

    Returns
    -------
    audio file
    """
    channels = 2 if (samples.ndim == 2 and samples.shape[1] == 2) else 1
    if normalized:
        y = np.int16(samples * 2 ** 15)
    else:
        y = np.int16(samples)
    audio = pydub.AudioSegment(
        y.tobytes(), frame_rate=frame_rate, sample_width=2, channels=channels)
    audio.export(audio_name, format="mp3", bitrate="320k")
