import pandas as pd
import numpy as np
from data_processing import *
from pipeline_functions.single_function_DQMs import channel_completeness


def compute_SCR(user_data_list):
    """
    Input: 
        user_data_list: A list represents a user's data, which is the same as the list
                        returned by load_data_pd_single in load_data.py.
    Return:
        The SCR for this user
    """
    SCR_sensor = []
    for sensor in user_data_list:
        feature_name = get_feature_name(sensor)
        channel_complete = []
        for record_df in sensor:
            record_list = record_df_to_dict(record_df)
            channel_complete.append(channel_completeness(record_list, feature_name))
        if len(channel_complete)>0:
            SCR_sensor.append(sum(channel_complete)/len(channel_complete))
    return np.mean(SCR_sensor)


def compute_SCR_single(record_df):
    feature_name = get_feature_name_record_df(record_df)
    record_list = record_df_to_dict(record_df)
    SCR = channel_completeness(record_list, feature_name)
    return SCR


def compute_SCR_multiple(data_list):
    SCR_list = []
    for record in data_list:
        record_SCR = compute_SCR_single(record)
        SCR_list.append(record_SCR)
    return np.mean(SCR_list)