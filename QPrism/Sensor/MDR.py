import pandas as pd
import numpy as np
from QPrism.Sensor.data_processing import *
from QPrism.Sensor.pipeline_functions.preprocessing import *
from QPrism.Sensor.pipeline_functions.single_function_DQMs import *


def compute_MDR_single(record_df):
    sample_consistence, sample_rate_median, sample_mode = sampling_rate_consistency(record_df)
    MDR = count_missing_segments(record_df, sample_mode)
    return MDR


def compute_MDR_multiple(data_list):
    MDR_list = []
    for record in data_list:
        record_MDR = compute_MDR_single(record)
        MDR_list.append(record_MDR)
    return np.mean(MDR_list)
