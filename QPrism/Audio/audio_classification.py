import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import csv
from scipy import signal
from scipy.io import wavfile


def audio_classification(wav_path):
    """
    Get a list of all the sounds in an audio

    This function returns a list of all the prominent sounds inside the audio

    Parameters
    -----------
    wav_path : path to a .wav audio

    Returns
    -------
    list: all sounds in an audio
        ['Speech', 'Whistling', 'Alarm']
    """

    model = hub.load('https://tfhub.dev/google/yamnet/1')

    def class_names_from_csv(class_map_csv_text):
        """Returns list of class names corresponding to score vector."""
        class_names = []
        with tf.io.gfile.GFile(class_map_csv_text) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                class_names.append(row['display_name'])

        return class_names

    class_map_path = model.class_map_path().numpy()
    class_names = class_names_from_csv(class_map_path)

    def ensure_sample_rate(original_sample_rate, waveform,
                           desired_sample_rate=16000):
        """Resample waveform if required."""
        if original_sample_rate != desired_sample_rate:
            desired_length = int(round(float(len(waveform)) /
                                       original_sample_rate * desired_sample_rate))
            waveform = signal.resample(waveform, desired_length)
        return desired_sample_rate, waveform

    sample_rate, wav_data = wavfile.read(wav_path, 'rb')
    sample_rate, wav_data = ensure_sample_rate(sample_rate, wav_data)

    waveform = wav_data / tf.int16.max

    scores, embeddings, spectrogram = model(waveform)

    scores_np = scores.numpy()
    probs = scores_np.mean(axis=0)
    ind = np.where(probs >= 0.1)
    infered_class = []
    for indi in ind[0]:
        infered_class.append(class_names[indi])
    return infered_class
