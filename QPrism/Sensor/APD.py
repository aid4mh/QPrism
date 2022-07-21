import pandas as pd
import numpy as np
from QPrism.Sensor.data_processing import *
from QPrism.Sensor.pipeline_functions.outlier_detection import count_outliers


def compute_APD_single(record_df):
    feature_name = get_feature_name_record_df(record_df)
    outlier_percent, outlier_rows = count_outliers(record_df, feature_name)
    global outlier_index
    outlier_index = outlier_rows
    return outlier_percent


def compute_APD_multiple(data_list):
    APD_list = []
    for record in data_list:
        record_APD = compute_APD_single(record)
        APD_list.append(record_APD)
    return np.mean(APD_list)
