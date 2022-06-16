import os 


def audio_paths(audio_dir):
    """
    Get the paths of the audio files

    This function stores the paths of all audio files in a list

    Parameters
    -----------
    audio_dir : directory containing all the audio diaries

    Returns
    -------
    list
        ['/path/to/audio_file1', '/path/to/audio_file2', ... '/path/to/audio_filen']
    """

    audio_paths = []
    for filename in os.listdir(audio_dir):
        if not filename.startswith('.'):
            audio_paths.append(str(os.path.join(audio_dir, filename)))

    return audio_paths