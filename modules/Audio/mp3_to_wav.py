from pathlib import Path
from os import path
from pydub import AudioSegment


def mp3_wav(mp3_path):
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
    audio_name = str(Path(mp3_path).stem)
    wav_name = Path(audio_name + "_Wav.wav")

    sound = AudioSegment.from_mp3(mp3_path)
    sound = sound.set_channels(1)
    sound.export(wav_name, format="wav")
