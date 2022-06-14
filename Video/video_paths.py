import os


def video_paths(video_dir):
    """
    Get the paths of the video files

    This function stores the paths of all video files in a list

    Parameters
    -----------
    video_dir : directory containing all the video diaries

    Returns
    -------
    list
        ['/path/to/video_file1', '/path/to/video_file2', ... '/path/to/video_filen']
    """

    video_paths = []
    for filename in os.listdir(video_dir):
        if not filename.startswith('.'):
            video_paths.append(os.path.join(video_dir, filename))
    return video_paths