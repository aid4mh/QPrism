import pandas as pd
import numpy as np
from QPrism.Sensor.data_processing import *
from QPrism.Sensor.pipeline_functions.single_function_DQMs import valid_data_ratio


def compute_VDR_single(record_df):
    feature_name = get_feature_name_record_df(record_df)
    VDR = valid_data_ratio(record_df, feature_names=feature_name)
    return VDR


def compute_VDR_multiple(data_list):
    VDR_list = []
    for record in data_list:
        record_VDR = compute_VDR_single(record)
        VDR_list.append(record_VDR)
    return np.mean(VDR_list)