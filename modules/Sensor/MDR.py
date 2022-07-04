import pandas as pd
import numpy as np
from data_processing import *
from pipeline_functions.preprocessing import *
from pipeline_functions.single_function_DQMs import *


def compute_MDR_single(record_df):
    r_time = record_df.iloc[-1][(list(record_df.keys()))[0]] - record_df.iloc[0][(list(record_df.keys()))[0]]
    feature_name = get_feature_name_record_df(record_df)
    sample_consistence, sample_rate_median, sample_mode = sampling_rate_consistency(record_df)
    record_df = standard_scaler(record_df, feature_name)
    record_df = multi_var_to_uni(record_df, feature_name)
    missing_t, missing_segment_count, filled_record = count_missing_segments(record_df, sample_mode)
    return missing_t/(r_time if r_time>missing_t else missing_t)


def compute_MDR_multiple(data_list):
    MDR_list = []
    for record in data_list:
        record_MDR = compute_MDR_single(record)
        MDR_list.append(record_MDR)
    return np.mean(MDR_list)
