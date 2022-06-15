from pathlib import Path
from os import path
from pydub import AudioSegment

def mp3_to_wav(mp3_path):

    audio_name = str(Path(mp3_path).stem)
    wav_name = Path(audio_name + "_Wav.wav")

    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(wav_name, format="wav")
