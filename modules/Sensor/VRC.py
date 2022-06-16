import pandas as pd
import numpy as np
from pipeline_functions.single_function_DQMs import *
from data_processing import *


def compute_VRC(user_data_list):
    """
    Input: 
        user_data_list: A list represents a user's data, which is the same as the list
                        returned by load_data_pd_single in load_data.py.
    Return:
        The VRC for this user
    """
    VRC_sensor = []
    for sensor in user_data_list:
        feature_name = get_feature_name(sensor)
        min_max = []
        for record_df in sensor:    
            record_list = record_df_to_dict(record_df) 
            min_max.append(minmax(record_list, feature_name))
        if (len(min_max)>0):
            VRC_sensor.append(consistency(min_max))
    return np.mean(VRC_sensor)


def compute_VRC_multiple_file(data_list):
    min_max = []
    for record_df in data_list:
        feature_name = get_feature_name_record_df(record_df)
        record_list = record_df_to_dict(record_df)
        min_max.append(minmax(record_list, feature_name))
    return consistency(min_max)