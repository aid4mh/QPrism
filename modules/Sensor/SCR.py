import pandas as pd
import numpy as np
from data_processing import *
from pipeline_functions.single_function_DQMs import channel_completeness


def compute_SCR_single(record_df):
    feature_name = get_feature_name_record_df(record_df)
    record_list = record_df_to_dict(record_df)
    SCR = channel_completeness(record_list, feature_name)
    return SCR


def compute_SCR_multiple(data_list):
    SCR_list = []
    for record in data_list:
        record_SCR = compute_SCR_single(record)
        SCR_list.append(record_SCR)
    return np.mean(SCR_list)