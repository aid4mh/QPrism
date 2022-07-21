# QPrism

## Statement of Need
While the number of research involving heterogeneous datasets is rapidly increasing, with the big data market having a Compound Annual Growth Rate (CAGR) of 13.2% (Statista, 2022), there isn't a dedicated package that allows researchers to perform data-driven data quality assessment on heterogeneous real-world datasets. Nevertheless, a limited number of existing libraries  contain single-type data quality assessment functions, mostly relying on application-specific data assumptions. For audio, the avaible packages' major area of interest is music data processing and visualization e.g. Python-based Librosa and Audioop and R-based Essentia. For video data quality assessment, we only found the QVA package, which aims at making sub-groups in a video dataset based on similar qualities and requires the user to be on a Windows machine. For sensor data, each of the available quality assessment packages is restricted to a specific data quality aspect. For instance, PyOD contains a range of functions for outlier detection, while SciPy provides outlier detection and signal-to-noise ratio (SNR) computation functions. However, there is no existing open-source package which performs sensor data quality assessment on across multiple dimensions e.g. completeness, correctness, and consistency. 

QPrism fills the current gap by allowing researchers and developers to perform data quality analysis, and devise plans for pre-analytical quality control plans. Thus, QPrism covers the need for having access to a broad spectrum of data quality metrics in a single Python package for comprehensive exploration of heterogeneous data. 


## Installation

    The installation can be done with pip, this will automatically install all the dependencies.

    ` $ (sudo) pip install QPrism `


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
   
   [MIT License](https://github.com/aid4mh/QPrism/blob/main/LICENSE)
    
