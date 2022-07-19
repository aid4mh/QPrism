from scipy.io import wavfile


def audio_length(wav_path):
    """
    Get the length of an audio

    This function takes the path of a wav audio file and returns its length

    Parameters
    -----------
    wav_path : path of a .wav audio

    Returns
    -------
    float: the length of the audio file in seconds
        "104.5"
    """
    sample_rate, wav_data = wavfile.read(wav_path, 'rb')
    duration = len(wav_data)/sample_rate
    return round(float(duration), 3)
