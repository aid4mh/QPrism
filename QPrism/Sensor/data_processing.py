import pandas as pd
import numpy as np


def get_feature_name_record_df(record_df):
    keys = list(record_df.keys())
    keys.remove(keys[0])
    return keys


def scale_data(data):
    scaled_data = (data - np.min(data)) / (np.max(data) - np.min(data))
    scaled_data = pd.DataFrame(scaled_data)
    scaled_data.columns = data.columns
    return scaled_data