import os
from statistics import mean

import speech_recognition as sr

from pydub import AudioSegment
from pydub.utils import make_chunks

          
def audio_translate(audio_name):   
        """
        This function translate the given audio file into text using the Google API

        Parameters
        ----------
        audio_name : name of the audio_file

        Returns
        -------
        string, float
                "some text ", 0.6754368
        """ 

        print("Translating ", audio_name)

        # Make a directory to store the audio chunks
        chunks_folder = 'audio_chunks'
        os.makedirs(chunks_folder, exist_ok=True)
        
        # Convert to .wav format
        sound = AudioSegment.from_mp3(audio_name)
        sound.export("audio.wav", format="wav")

        # Split the large audio file into smaller chunks
        chunks = make_chunks(sound, 10000)

        # Initialize the Recognizer
        r = sr.Recognizer()

        # Make a empty variable for text and it's confidence
        recognized = ""
        acc = []

        # Translate
        for i, chunk in enumerate(chunks):
                chunk_name = os.path.join(chunks_folder, "{0}.wav".format(i))
                chunk.export(chunk_name, format="wav")
                with sr.AudioFile(chunk_name) as source:
                        audio = r.record(source) 
                        text = r.recognize_google(audio, language='en-US', show_all=True)
                        if not len(text) == 0:
                                recognized = recognized + text['alternative'][0]['transcript'] + " "
                                acc.append(text['alternative'][0]['confidence'])
        
        return recognized, mean(acc)