# QPrism

## Statement of Need
QPrism is a python module that contains all the functions needed to understand the quality and accurately assess video, audio, or sensor data. A user can get the relevant metrics for an individual data point or use the pipeline that loops over all of the data and creates a CSV file containing their metrics. QPrism can be used for multiple research or development projects for explaratory data analysis and quality assurance of video, audio, or sensor data. While this type of data is very popular and rapidly increasing, there isn't is well-known library that deals with explaratory data analysis for it. Quality assessment is a cruitial step in every Machine Learning or Deep Learning project which can highly affect the results and bias of the model. Thus, QPrism can aid many researchers and developers in exploring their data, eliminating any outliers or bias, and improve the quality and clarity of their work.

## Installation

 ### Dependencies: 
 1. For Video:
 
 | Library                                          | Version         | Installation                                |
| :-------------------------------------------------- | :-------------- | :------------------------------------------ |
| [ffmpeg](https://www.ffmpeg.org/download.html)      | 5.0.1 "Lorentz" | `pip install ffprobe `                      |
| [numpy](https://numpy.org/)                         | 1.22.4          | `pip install numpy`                         |
| [opencv-python](https://opencv.org/)                | 4.5.5           | `pip install opencv-python `                |
| [Pillow](https://pillow.readthedocs.io/en/stable/)  | 9.1.1           | `pip install Pillow`                        |
| [torch](https://pytorch.org/docs/stable/torch.html) | 1.22            | `pip3 install torch torchvision torchaudio` |

2. For Audio:

| Library                                          | Version         | Installation                                |
| :-------------------------------------------------- | :-------------- | :------------------------------------------ |
| [tensoflow](https://www.tensorflow.org/versions) <br> AppleChip: [tensorflow-macos](https://developer.apple.com/metal/tensorflow-plugin/) | 2.9| `pip install tensorflow` |
|[tensorflow-hub](https://pypi.org/project/tensorflow-hub/)| 0.12.0 | `pip install tensorflow-hub`|
|[scipy](https://scipy.org) | 1.8.0 | `pip install scipy`|
| [numpy](https://numpy.org/)                         | 1.22.4          | `pip install numpy`                         |
|[pydub](https://pypi.org/project/pydub/)|0.25.1|`pip install pydub`|

4. For Sensor:

| Library                                          | Version         | Installation                                |
| :-------------------------------------------------- | :-------------- | :------------------------------------------ |
| [pandas]([https://www.tensorflow.org/versions](https://pandas.pydata.org/docs/getting_started/install.html)) | 1.4.2| `pip install pandas` |

 ### Installation: 
      - `Conda`
      - `pip`
      - `git clone`

## Basic Usage

  ## Functions & Definitions: 
  1. Video: 
 
| Function                       | Input                                                                                                                                           | Output                                                                                                             |
| :----------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| `get_format(path)`             | **path** `str`: path to a specific video                                                                                                        | **format** <br>`str`: video format \_ex ".mp4", ".mov",...                                                         |
| `get_resolution(path)`         | **path** `str`: path to a specific video                                                                                                        | **resolution** <br>`str`: string containing the resolution of the video <br> `str` "720p"                          |
| `get_length(path)`             | **path** `str`: path to a specific video or directory that contains all the videos                                                              | **length** <br>`int`: video length (seconds) <br>`list` : [101, ... 67]                                            |
| `get_objects(path, modelname)` | **path** `str`: path to a specific video or directory that contains all the videos <br> **modelname** `str`: name of the object detection model | **Objects detected** <br> `dict`: {'person', 'dog'}                                                                |
| `get_framerate(path)`          | **path** `str`: path to a specific video \                                                                                                      | **frame rate** <br> `int`: framerate of specific video                                                             |
| `get_bitrate(path)`            | **path** `str`: path to a specific video                                                                                                        | **bit rate** <br> `int`: bit rate of specific video                                                                |
| `get_brightness(path)`         | **path** `str`: path to a specific video                                                                                                        | **brightness** `int`: brightness of specific video                                                                 |
| `get_creation_time(path)`      | **path** `str`: path to a specific video                                                                                                        | **creation time** `str`: the date and time of when the video was created <br> `str` : "2022-05-29 23:22:59.599607" |
| `get_artifacts(path)`      | **path** `str`: path to a specific video                                                                                                        | **percentage artifacts** `int`: the percentage of the video that contains artifacts (motion blur, too grainy, static) <br> `int` : "3.351" |

2. Audio: 

| Function                | Input                                                                                                                                                  | Output                                                                                                          |
| :---------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------- |
| `get_audio(path)`       | **path** `str`: path to a specific video                                                                                                               | **None** <br> Extracts and stores the audio under a folder called `audio_files`                                 |
| `get_audio_classification(wav_path)` | **wav_path** `str`: path of a .wav audio                                                                                                               | **sounds in audio** `list`: a list of the sounds inside the audio <br> `list` : ['Speech', 'Whistling', 'Alarm'] |
| `get_audio_length(wav_path)` | **wav_path** `str`:  path of a .wav audio  | **audio length** `int`: the length of the audio file in seconds <br> `int`: "104.5" |
| `get_audio_sample_rate(wav_path)` | **wav_path** `str`:  path of a .wav audio  | **audio frame rate** `int`: the frame rate of the audio <br> `int`: "16000" |
| `get_mp3_to_wav(mp3_path)` | **mp3_path** `str`:  path of a .mp3 audio  | **NONE** saves the .wav audio in the same working directory |
| `get_audio_to_text(audio_name)` | **wav_path** `str`:  path of a .wav audio | **translated text** `str`: the speech in the audio transcribed <br> **Accuracy** `int`: the accuracy of teh translation |
| `get_text_punctuate(csv_path, text_col)` | **csv_path** `str`:  path to the csv file <br> **text_col** `str`: the name of the column that contains the text | **NONE** saves the modified csv file to working directory <br> "Hi Im Alex" to "Hi, I'm Alex."|

3. Sensor:

| Function                     | Input                                                                                     | Output |
| :--------------------------- | :---------------------------------------------------------------------------------------- | :----- |
| `set_input_path(self, path)` | **path** (`str`): Path to the folder contains users' data.                                | `None` |
| `set_RLC(self, included)`    | **included** (`bool`): A bool value to indicate whether RLC is included in the result DQM | `None` |
| `set_SNR(self, included)`    | **included** (`bool`): A bool value to indicate whether SNR is included in the result DQM | `None` |
| `set_VRC(self, included)`    | **included** (`bool`): A bool value to indicate whether VRC is included in the result DQM | `None` |
| `set_SCR(self, included)`    | **included** (`bool`): A bool value to indicate whether SCR is included in the result DQM | `None` |
| `set_SRC(self, included)`    | **included** (`bool`): A bool value to indicate whether SRC is included in the result DQM | `None` |
| `set_MDR(self, included)`    | **included** (`bool`): A bool value to indicate whether MDR is included in the result DQM | `None` |
| `set_APD(self, included)`    | **included** (`bool`): A bool value to indicate whether APD is included in the result DQM | `None` |
| `compute_DQMs(self)`         | `None`                                                                                    | `None` |
| `save_to_file(self, path)`   | **path** (`str`): Path to the output csv file.                                            | `None` |

An explanation of the metrics supported for sensor QA:

| Term   | Definition                                                                                                  | Category     |
| :----- | :---------------------------------------------------------------------------------------------------------- | :----------- |
| `APD`  | Anomalous Points Density - Ratio of outliers/anomalous data samples by the total number of samples.         | Correctness  |
| `DQM`  | Data Quality Matrix - Matrix generated by the pipeline to demonstrate data quality.                         | N/A          |
| `IRLR` | Interpretable Record Length Ratio - Ratio of records having non-zero length by the total number of records. | Completeness |
| `MDR`  | Missing Data Ratio - Ratio of missing data samples by the total number of samples.                          | Completeness |
| `RLC`  | Record Length Consistency - Uniformness of data record length within and across sensors.                    | Consistency  |
| `SCR`  | Sensor Channel Ratio - Ratio of recorded sensor channels by the typical number of records.                  | Completeness |
| `SNR`  | Signal-to-noise Ratio - Ratio of the desired signal amplitude by the noise amplitude.                       | Correctness  |
| `SRC`  | Sampling Rate Consistency - Uniformness of the sampling rate within and across records.                     | Consistency  |
| `VRC`  | Value Range Consistency - Uniformness of the value range within and across records.                         | Consistency  |


## Examples:
1. Video:


Code: `Video = qprism.Video()` <br>
`framerate = Video.framerate(path='example_video.mp4')` <br>
`print("Frame rate of the video is", framerate)
`

output: `Frame rate of the video is 60`

2. Audio:

Code: `Audio = qprism.Audio()` <br>
`sounds = Audio.classification(path='example_video.mp4')` <br>
`print("Sounds in the audio are:", sounds)`

output: `Sounds in the audio are: ['Speech', 'Whistling', 'Alarm']`

3. Sensor: 

Code: `Sensor = qprism.Sensor()` <br>

output:


## Demo notebooks

  - sensor demo notebook
  - [Video demo notebook](https://github.com/aid4mh/QA-module/blob/main/demo_video.ipynb)
  - audio demo notebook


## Contributing to the project


# Acknowledgments


# Authors
- [@Ramzi Halabi](https://github.com/RamziHalabi)
- [@RahaviSelvarajan](https://github.com/RahaviSelvarajan)
- [@Jana-kabrit](https://github.com/Jana-kabrit)
- [@ZixiongLin1](https://github.com/ZixiongLin1)


# Contact 

- to report issues 
- to seek support


# License
   
    
