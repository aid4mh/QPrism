import pandas as pd
import numpy as np
from QPrism.Sensor.pipeline_functions.single_function_DQMs import consistency


def compute_RLC(user_data_list):
    """
    Input: 
        user_data_list: A list represents a user's data, which is the same as the list
                        returned by load_data_pd_single in load_data.py.
    Return:
        The RLC for this user
    """
    RLC_sensor = []
    for sensor in user_data_list:
        record_lengths = []
        for record_df in sensor:
            record_lengths.append(len(record_df))
        RLC_sensor.append(consistency(record_lengths))
    return np.mean(RLC_sensor)


def compute_RLC_multiple_file(data_list):
    record_lengths = []
    for record_df in data_list:
        record_lengths.append(len(record_df))
    return consistency(record_lengths)
        