import pandas as pd
import numpy as np
from QPrism.Sensor.data_processing import *
from QPrism.Sensor.pipeline_functions.signal_to_noise import *


def compute_SNR_single(record_df):
    feature_name = get_feature_name_record_df(record_df)
    SNR = snr(record_df, feature_names=feature_name)
    return SNR


def compute_SNR_multiple(data_list):
    SNR_list = []
    for record in data_list:
        record_SNR = compute_SNR_single(record)
        SNR_list.append(record_SNR)
    return np.mean(SNR_list)
    