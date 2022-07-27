# QPrism

## Statement of Need
While the healthcare big data market is projected to increase from around 11.5 billion to nearly 70 billion U.S. dollars between 2016 and 2025 (Statista, 2022), there isn't a comprehensive package that allows researchers to perform data-driven quality assessment on multimodal real-world digital health data. In fact, data quality covers multiple dimensions e.g. completeness, correctness, consistency, which ought to be jointly investigated for the quantitative assessment of data availability and usability prior to data analysis. This calls for the development of multimodal sensor data quality metrics (DQM),  ideally in a single module, permitting well-rounded quality assessment and reporting for researchers and analysts.

Despite the major need for such quality assessment packages in digital health and across all data analytical fields, the currently available tools partially address the scientists’ and analysts’ needs. The available functions are mostly data descriptive metrics that require further contextualization and application-specific tuning to be used as DQMs, and the available modules and packages cover a single quality dimension e.g. noise level, anomaly level, object detection. For instance, PyOD contains a wide range of functions for outlier detection, while SciPy provides signal-to-noise ratio (SNR) computation functions as well as statistical descriptors that may be customized as DQMs. Specifically for audio, Python-based Librosa and Audioop, and R-based Essentia provide functions for audio processing and feature extraction, requiring further development to serve as DQMs. Lastly, for video data quality assessment, the QVA package performs common quality-based video clustering, however requiring the user to be on a Windows machine. 

QPrism fills the current gap by allowing researchers and developers to perform data quality analysis, and devise plans for pre-analytical quality control plans. Thus, QPrism covers the need for having access to a broad spectrum of data quality metrics in a single Python package for comprehensive data-driven quality assessment of real-word data. 



## Installation

The installation can be done with pip. since pip does not resolve the dependencies' version efficiently, please install QPrism with the following steps.

  ```
  $ python3 -m pip install --upgrade pip
  ```

  ```
  $ pip install -r https://raw.githubusercontent.com/aid4mh/QPrism/main/requirements.txt
  ```

  ```
  $ pip install --no-deps -i https://test.pypi.org/simple/ QPrism==0.1.6
  ```


## Documentation

The full documentation for QPrism can be accessed [here](https://qprism.readthedocs.io/en/latest/).
 



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

  - [sensor demo notebook](https://github.com/aid4mh/QPrism/tree/main/tests/Sensor)
  - [Video demo notebook](https://github.com/aid4mh/QA-module/blob/main/demo_video.ipynb)
  - audio demo notebook


# Contributing to the project


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
   
   [MIT License](https://github.com/aid4mh/QPrism/blob/main/LICENSE)
    
