import pandas as pd
import numpy as np
from data_processing import *
from pipeline_functions.outlier_detection import count_outliers



def compute_APD(user_data_list):
    """
    Input: 
        user_data_list: A list represents a user's data, which is the same as the list
                        returned by load_data_pd_single in load_data.py.
    Return:
        The SRC for this user
    """
    APD_sensor = []
    for sensor in user_data_list:
        feature_name = get_feature_name(sensor)
        outlier_percents = []
        for record_df in sensor:
            record_list = record_df_to_dict(record_df)
            outlier_percent, outlier_locations = count_outliers(record_list, feature_name,'standard','2_step')
            outlier_percents.append(outlier_percent)
        if (len(outlier_percents)>0):
            APD_sensor.append(np.mean(outlier_percents))
    return np.mean(APD_sensor)


def compute_APD_single(record_df):
    feature_name = get_feature_name_record_df(record_df)
    record_list = record_df_to_dict(record_df)
    outlier_percent, outlier_locations = count_outliers(record_list, feature_name,'standard','2_step')
    return outlier_percent


def compute_APD_multiple(data_list):
    APD_list = []
    for record in data_list:
        record_APD = compute_APD_single(record)
        APD_list.append(record_APD)
    return np.mean(APD_list)