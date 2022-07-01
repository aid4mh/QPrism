from pathlib import Path
from os import path
from pydub import AudioSegment
import os


def to_mono_wav(aud_path):
    """
    Convert mp3 files to mono wav files

    This function takes in mp3 audio files and converts them into mono wav files to be used for deep learning and further exploration.

    Parameters
    -----------
    mp3_path : path to the .mp3 file

    Returns
    -------
    NONE
        Saves the .wav file in the same working directory
        "audio_Wav.wav"
    """
    split_tup = os.path.splitext(aud_path)
    format = (split_tup[-1])

    if str(format) == '.wav':
        sound = AudioSegment.from_wav(aud_path)
        sound = sound.set_channels(1)
        audio_name = str(Path(aud_path).stem)
        wav_name = Path(audio_name + "_Mono.wav")
        sound.export(wav_name, format="wav")
    elif str(format) == '.mp3':
        sound = AudioSegment.from_mp3(aud_path)
        sound = sound.set_channels(1)
        audio_name = str(Path(aud_path).stem)
        wav_name = Path(audio_name + "_Wav.wav")
        sound.export(wav_name, format="wav")
    else:
        "Please enter an .mp3 or .wav file"
