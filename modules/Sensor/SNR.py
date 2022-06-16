import pandas as pd
import numpy as np
from data_processing import *
from pipeline_functions.signal_to_noise import *


def compute_SNR(user_data_list):
    """
    Input: 
        user_data_list: A list represents a user's data, which is the same as the list
                        returned by load_data_pd_single in load_data.py.
    Return:
        The SNR for this user
    """
    SNR_sensor = []
    for sensor in user_data_list:
        feature_name = get_feature_name(sensor)
        snr_avg = []
        for record_df in sensor:
            record_list = record_df_to_dict(record_df)
            snr_value = snr(record_list, feature_names=feature_name)
            snr_avg.append(snr_value)
        if(len(snr_avg)>0):
            SNR_sensor.append(np.mean(snr_avg))
    return np.mean(SNR_sensor)


def compute_SNR_single(record_df):
    feature_name = get_feature_name_record_df(record_df)
    record_list = record_df_to_dict(record_df)
    snr_value = snr(record_list, feature_names=feature_name)
    return snr_value


def compute_SNR_multiple(data_list):
    SNR_list = []
    for record in data_list:
        record_SNR = compute_SNR_single(record)
        SNR_list.append(record_SNR)
    return np.mean(SNR_list)
    