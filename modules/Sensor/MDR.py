import pandas as pd
import numpy as np
from data_processing import *
from pipeline_functions.preprocessing import *
from pipeline_functions.single_function_DQMs import *


def compute_MDR(user_data_list):
    """
    Input: 
        user_data_list: A list represents a user's data, which is the same as the list
                        returned by load_data_pd_single in load_data.py.
    Return:
        The MDR for this user
    """
    MDR_sensor = []
    for sensor in user_data_list:
        feature_name = get_feature_name(sensor)
        missing_time = []
        for record_df in sensor:
            r_time = record_df['records'][len(record_df)-1]['timestamp']-record_df['records'][0]['timestamp']
            record_list = record_df_to_dict(record_df)
            sample_consistence, sample_rate_median, sample_mode = sampling_rate_consistency(record_list)
            record_list = standard_scaler(record_list, feature_name)
            record_list = multi_var_to_uni(record_list, feature_name)
            missing_t, missing_segment_count, filled_record = count_missing_segments(record_list, sample_mode)
            missing_time.append(missing_t/(r_time if r_time>missing_t else missing_t))
        if (len(missing_time)>0):
            MDR_sensor.append(np.mean(missing_time))
    return np.mean(MDR_sensor)


def compute_MDR_single(record_df):
    r_time = record_df['records'][len(record_df)-1]['timestamp']-record_df['records'][0]['timestamp']
    feature_name = get_feature_name_record_df(record_df)
    record_list = record_df_to_dict(record_df)
    sample_consistence, sample_rate_median, sample_mode = sampling_rate_consistency(record_list)
    record_list = standard_scaler(record_list, feature_name)
    record_list = multi_var_to_uni(record_list, feature_name)
    missing_t, missing_segment_count, filled_record = count_missing_segments(record_list, sample_mode)
    return missing_t/(r_time if r_time>missing_t else missing_t)


def compute_MDR_multiple(data_list):
    MDR_list = []
    for record in data_list:
        record_MDR = compute_MDR_single(record)
        MDR_list.append(record_MDR)
    return np.mean(MDR_list)
