import pandas as pd
import time
from load_data import *
import numpy as np
from data_processing import *
from pipeline_functions.preprocessing import features_to_float


def std_arr(arr):
    """
    Return the standard deviation for given array
    """
    arr = arr - np.mean(arr)
    arr = np.asarray(arr)
    std_dev = arr.std(axis=0, ddof=1)
    return std_dev


def get_df_feature_name(df):
    """
    Input:
        df: A dataframe
    Return:
        keys: A list of str represents the feature name of given sensor
    """
    # return -1 if the sensor has no record
    record_df = df
    keys = list(record_df.keys())
    keys.remove(keys[0])
    return keys


def compute_IRLR_single(record_df):
    feature_names = get_df_feature_name(record_df)
    if (len(record_df)<2):
        return 0
    elif (int(record_df.iloc[[len(record_df)-1]][(list(record_df.keys()))[0]])-int(record_df.iloc[[0]][list(record_df.keys())[0]]))<=0:
        return 0
    else:
        #record_list = record_df_to_dict(record_df)
        record = features_to_float(record_df, feature_names)
        std_values = []
        for feature in feature_names:
            std_values.append(std_arr(record[feature].values))
        for std_value in std_values:
            if (std_value==0):
                return 0
    return 1


def compute_IRLR_multiple(data_list):
    record_count = 0
    insufficient_length_count = 0
    delete_list = []
    for i in range (len(data_list)):
        record_df = data_list[i]
        # remove records has length <= 2
        if (len(record_df)<2):
            insufficient_length_count += 1
            delete_list.append(i)
        # remove records with same starting and ending timestamp
        elif (record_df[len(record_df)-1][(list(record_df[len(record_df)-1].keys()))[0]]-record_df[0][list(record_df[0].keys())[0]])<=0:
            insufficient_length_count += 1
            delete_list.append(i)
        # remove records with 0 std or missing channels
        else:
            feature_names = get_df_feature_name(record_df)
            record_list = record_df_to_dict(record_df)
            record = features_to_float(record_list, feature_names)
            std_values = [std_arr([r[feature] for r in record]) for feature in feature_names]
            for std_value in std_values:
                if (std_value==0):
                    insufficient_length_count += 1
                    delete_list.append(i)
                    break
        record_count += 1
    j = 0
    # delete all the insufficient records
    for index in delete_list:
        del data_list[index-j]
        j += 1
    return 1-(insufficient_length_count/record_count)


if __name__ == '__main__':
    stime_pd = time.time()
    data_list_pd = load_data_pd_single_file('/home/lin/Documents/CAMH/SenseActivity/data/Test/SUBJ00001/Accelerometer/SUBJ00001_Accelerometer_REC000000.json')
    etime_pd = time.time()
    print("The processing time for load data into pandas is: " + str(etime_pd-stime_pd) + ' seconds.')
    # testing IRLR
    print("The IRLR score is: " + str(compute_IRLR_single(data_list_pd)))