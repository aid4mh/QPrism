# Video Quality Assessment

## 👩‍💻 Authors

- [@RahaviSelvarajan](https://github.com/RahaviSelvarajan)
- [@Jana-kabrit](https://github.com/Jana-kabrit)
- [@ZixiongLin1](https://github.com/ZixiongLin1)

## 📝 Goal/Objective:

- To create a python module which can be imported into projects and used for assessing the quality of video, audio, and sensor data.

## 🛠 Requirements

### To download:

| Libraries                                           | Version         | Installation                                |
| :-------------------------------------------------- | :-------------- | :------------------------------------------ |
| [ffmpeg](https://www.ffmpeg.org/download.html)      | 5.0.1 "Lorentz" | `pip install ffprobe `                      |
| [numpy](https://numpy.org/)                         | 1.22.4          | `pip install numpy`                         |
| [opencv-python](https://opencv.org/)                | 4.5.5           | `pip install opencv-python `                |
| [Pillow](https://pillow.readthedocs.io/en/stable/)  | 9.1.1           | `pip install Pillow`                        |
| [torch](https://pytorch.org/docs/stable/torch.html) | 1.22            | `pip3 install torch torchvision torchaudio` |

## 🏃🏻‍♀️ How to run

Clone the repository into your project directory using the following command.

```bash
git clone https://github.com/aid4mh/QA-module.git
```

Now import the QA-module module for QA metrics calculation.

```bash
import QA-module as qamod
```

### Use case 1 - accel data (all metrics)

qamod.qa_metric(data_file=”/path/accel/file”, type=’sensor’, metric=’all’)
csv = q_metric.get_metrics()

### Use case 2 - accel data (1 file)

qamod.qa_metric(data_file=”/path/accel/file”, type=’sensor’, metric=’Specific’)

qamod.snr(data_file=”/path/accel/file”) -> return SNR value/s
qamod.irlr(data_file=”/path/accel/file”) -> return IRLR value/s

## 🚦 Quality Assessment Metrics Supported

In this module, we have defined 9 functions for different quality assessment metrics. The table below explains what each function is by its input and output.

### 🎥 Video QA:

#### Functions

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

#### Pipeline:

...TBA once the structure of the pipeline is decided upon (class/function). It will return a CSV file that contains the results of all the metrics for one/more than 1 data path.

### 🎙 Audio QA:

#### Functions:

| Function                | Input                                                                                                                                                  | Output                                                                                                          |
| :---------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------- |
| `get_audio(path)`       | **path** `str`: path to a specific video                                                                                                               | **None** <br> Extracts and stores the audio under a folder called `audio_files`                                 |
| `get_audio_array(path)` | **path** `str`: path to a specific audio                                                                                                               | **audio frame rate** `int`: the frame rate of the audio, **samples** `arr` the array representing the audio<br> |
| `get_array_audio(path)` | **path** `str`: path to a specific audio <br> **frames** `int`: the framerate of the audio <br> **samples** `arr` the array to be transformed to audio | **audio frame rate** `int`: the frame rate of the audio, **samples** `arr` the array representing the audio<br> |

### 🌡 Sensor QA

#### :book: Glossary

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

#### Sensor Functions

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

## 🔍 Object Detection

For object detection, supported [yolov5](https://docs.ultralytics.com/) models (for now) are

- yolov5s
- yolov5n
- yolov5m
- yolov5l
- yolov5x

A pretrained model on coco dataset is used for detecting objects in the video.
