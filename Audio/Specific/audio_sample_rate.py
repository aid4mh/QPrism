from scipy.io import wavfile

def sample_rate(wav_path):
    sample_rate, wav_data = wavfile.read(wav_path, 'rb')
    return int(sample_rate)
