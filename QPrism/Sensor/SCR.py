import pandas as pd
import numpy as np
from QPrism.Sensor.data_processing import *
from collections import Counter

def compute_SCR_multiple(data_list):
    channel_num_list = []
    incomplete_record_count = 0
    for df in data_list:
        channel_num_list.append(df.shape[1]-1)
    mode = Counter(channel_num_list).most_common(1)[0][0]
    for channel_num in channel_num_list:
        if channel_num != mode:
            incomplete_record_count += 1
    SCR = (len(channel_num_list)-incomplete_record_count)/len(channel_num_list)
    return SCR