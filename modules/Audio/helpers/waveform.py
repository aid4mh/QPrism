import matplotlib.pyplot as plt
import numpy as np
import wave
from pathlib import Path


def waveform(wav_path):
    """
    Get the waveform graph of an wav audio file.

    This function returns the time/signal waveform graph of a audio file.

    Parameters
    -----------
    wav_path : path to a .wav audio

    Returns
    -------
    Graph: wafeform graph
    """
    raw = wave.open(wav_path)
    signal = raw.readframes(-1)
    signal = np.frombuffer(signal, dtype="int16")
    f_rate = raw.getframerate()
    time = np.linspace(
        0,  # start
        len(signal) / f_rate,
        num=len(signal)
    )
    audio_name = str(Path(wav_path).stem)

    plt.figure(1)
    plt.title(audio_name + ' Sound Wave')
    plt.xlabel("Time")
    plt.plot(time, signal)
    plt.show()
