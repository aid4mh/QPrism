import librosa


def spectral_centroids(wav_path):
    """
    The spectral centroid is a measure used to characterise an audio spectrum by finding its center of mass. It is also connected to the brightness of a sound, which refers to the higher mid and treble parts of the frequency.

    This function returns the list of spectrial centroids in each frame.

    Parameters
    -----------
    wav_path: path to a .wav audio

    Returns
    -------
    list: list of centriods in each frame
        "[3697.44113997 1783.07014188 1696.00335286 ... 1149.56986893 1089.87566734
 1054.68442024]"
    """
    x, sr = librosa.load(wav_path)
    spectral_centroids = librosa.feature.spectral_centroid(x, sr=sr)[0]
    return spectral_centroids
