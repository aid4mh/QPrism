import pandas as pd
import numpy as np
from QPrism.Sensor.data_processing import *
from QPrism.Sensor.pipeline_functions.single_function_DQMs import sampling_rate_consistency


def compute_SRC_single(record_df):
    sample_consistence, sample_rate_median, sample_mode = sampling_rate_consistency(record_df)
    return sample_consistence


def compute_SRC_multiple(data_list):
    SRC_list = []
    for record in data_list:
        record_SRC = compute_SRC_single(record)
        SRC_list.append(record_SRC)
    return np.mean(SRC_list)