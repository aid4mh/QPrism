import os
import pandas as pd
import json


def load_data_json_single_file(path):
    f = open(path)
    try:
        json_file = json.load(f)
    except:
        return pd.DataFrame([])
    json_file = json.dumps(list(json_file['records']))
    record_df = (pd.read_json(json_file))
    record_df[list(record_df.keys())[0]] = record_df[list(record_df.keys())[0]].apply(lambda x: x.value)
    return record_df


def load_data_json_multi_file(path):
    data_list = []
    records = os.listdir(path)
    for record in records:
        record_path = path+'/'+record
        try:
            data_list.append(load_data_json_single_file(record_path))
        except:
            data_list.append(pd.DataFrame())
    return data_list


def load_data_csv_one_file(path):
    record_df = pd.read_csv(path)
    keys = list(record_df.keys())
    record_df = record_df.drop(keys[0], axis=1)
    return record_df


def load_data_csv_multi_file(path):
    data_list = []
    records = os.listdir(path)
    for record in records:
        record_path = path+'/'+record
        try:
            data_list.append(load_data_csv_one_file(record_path))
        except:
            data_list.append(pd.DataFrame())
    return data_list
