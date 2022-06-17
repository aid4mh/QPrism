from scipy.io import wavfile


def sample_rate(wav_path):
    """
    Get the sample rate of an audio

    This function returns the sample rate of a .wav audio

    Parameters
    -----------
    wav_path : the path of a .wav audio

    Returns
    -------
    int: sample rate of the audio
        "16000"
    """
    sample_rate, wav_data = wavfile.read(wav_path, 'rb')
    return int(sample_rate)
