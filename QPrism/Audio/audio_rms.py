import audioop
import wave


def rms(wav_path):
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
    wav = wave.open(wav_path)
    frames, width = wav.readframes(wav.getnframes()), wav.getsampwidth()
    aud_rms = audioop.rms(frames, width)
    return aud_rms
