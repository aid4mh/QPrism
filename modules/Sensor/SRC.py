import pandas as pd
import numpy as np
from data_processing import *
from pipeline_functions.single_function_DQMs import sampling_rate_consistency


def compute_SRC(user_data_list):
    """
    Input: 
        user_data_list: A list represents a user's data, which is the same as the list
                        returned by load_data_pd_single in load_data.py.
    Return:
        The SRC for this user
    """
    SRC_sensor = []
    for sensor in user_data_list:
        sample_rate_consistency = []
        for record_df in sensor:
            record_list = record_df_to_dict(record_df)
            sample_consistence, sample_rate_median, sample_mode = sampling_rate_consistency(record_list)
            sample_rate_consistency.append(sample_consistence)
        if (len(sample_rate_consistency)>0):
            SRC_sensor.append(np.mean(sample_rate_consistency))
    return np.mean(SRC_sensor)


def compute_SRC_single(record_df):
    record_list = record_df_to_dict(record_df)
    sample_consistence, sample_rate_median, sample_mode = sampling_rate_consistency(record_list)
    return sample_consistence


def compute_SRC_multiple(data_list):
    SRC_list = []
    for record in data_list:
        record_SRC = compute_SRC_single(record)
        SRC_list.append(record_SRC)
    return np.mean(SRC_list)