from pathlib import Path
from os import path
from pydub import AudioSegment


def mp3_to_wav(mp3_path):
    audio_name = str(Path(mp3_path).stem)
    wav_name = Path(audio_name + "_Wav.wav")

    sound = AudioSegment.from_mp3(mp3_path)
    sound = sound.set_channels(1)
    sound.export(wav_name, format="wav")


mp3_to_wav(
    '/Users/jana/Documents/GitHub/QA-module/Audios/example_video_1_Audio.mp3')
