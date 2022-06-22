import pandas as pd
import numpy as np
from pipeline_functions.single_function_DQMs import *
from data_processing import *


def compute_VRC_multiple_file(data_list):
    min_max = []
    for record_df in data_list:
        feature_name = get_feature_name_record_df(record_df)
        record_list = record_df_to_dict(record_df)
        min_max.append(minmax(record_list, feature_name))
    return consistency(min_max)