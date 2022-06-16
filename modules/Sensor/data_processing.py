import pandas as pd
import numpy as np


def get_feature_name(sensor):
    """
    Input:
        sensor: A list of dataframes represents a sensor
    Return:
        keys: A list of str represents the feature name of given sensor
    """
    # return -1 if the sensor has no record
    if len(sensor)==0:
        return -1
    record_df = sensor[0]
    keys = list(record_df["records"][0].keys())
    keys.remove('timestamp')
    return keys


def get_feature_name_record_df(record_df):
    keys = list(record_df["records"][0].keys())
    keys.remove('timestamp')
    return keys


def record_df_to_dict(record_df):
    """
    Input:
        record_df: The dataframe of a record
    Output:
        A list of dict, each dict is a single record
    """
    if len(record_df!=0):
        record = record_df['records']
        record_list = []
        for single_record in record:
            record_list.append(dict(single_record))
        return record_list
    else:
        return []


def scale_data(data):
    scaled_data = (data - np.min(data)) / (np.max(data) - np.min(data))
    scaled_data = pd.DataFrame(scaled_data)
    scaled_data.columns = data.columns
    return scaled_data