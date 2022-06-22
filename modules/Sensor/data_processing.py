import pandas as pd
import numpy as np


def get_feature_name_record_df(record_df):
    keys = list(record_df[0].keys())
    keys.remove(keys[0])
    return keys


def record_df_to_dict(record_df):
    """
    Input:
        record_df: The dataframe of a record
    Output:
        A list of dict, each dict is a single record
    """
    if len(record_df!=0):
        record_list = []
        for single_record in record_df:
            record_list.append(dict(single_record))
        return record_list
    else:
        return []


def scale_data(data):
    scaled_data = (data - np.min(data)) / (np.max(data) - np.min(data))
    scaled_data = pd.DataFrame(scaled_data)
    scaled_data.columns = data.columns
    return scaled_data