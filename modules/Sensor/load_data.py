import os
import pandas as pd
import time

def load_data_pd_single(path):
    '''
    Input: 
        path: The path to the folder represents a subject, consists of folders for each sensor.
    Return: 
        user_data_list: A list of list of dataframes, the out-most list represents a user,
                        the inner list represents a sensor, 
                        and contains dataframes represent the sensor's records.
    '''
    sensors = os.listdir(path)
    user_data_list = []
    zero_length_count = 0
    got_userID = False
    for sensor_name in sensors:
        user_data_list.append([])
        sensor_path = path+'/'+sensor_name
        records = os.listdir(sensor_path)
        for record in records:
            record_path = sensor_path+'/'+record
            try:
                record_df = pd.read_json(record_path)
                user_data_list[-1].append(record_df)
                if not got_userID:
                    userID = record_df['clientId'].values[0]
                    got_userID = True
            except:
                zero_length_count += 1
                # insert an empty dataframe if the record is empty
                user_data_list[-1].append(pd.DataFrame([]))
                if not got_userID:
                    userID = path
    # return None if there is no sensor or no actual data
    if got_userID is False:
        return None, None
    return user_data_list, userID


def load_data_pd(path):
    '''
    Input: 
        path: The path to the folder represents a subject, consists of folders for each sensor.
    Return: 
        A list consists of two lists. The first list represents the userIDs in given path,
        the second list is a list of list, consists of user_data_list returned by
        load_data_pd_single for each user.
    '''
    users = os.listdir(path)
    user_list = []
    all_data_list = []
    for username in users:
        user_data_list, userID = load_data_pd_single(path+'/'+username)
        if (not user_data_list == None) and (not userID == None): 
            user_list.append(userID)
            all_data_list.append(user_data_list)
    return [user_list, all_data_list]


def load_data_pd_single_file(path):
    try:
        record_df = (pd.read_json(path))['records']
    except:
        record_df = pd.DataFrame([])
    return record_df


def load_data_pd_multi_file(path):
    data_list = []
    records = os.listdir(path)
    for record in records:
        record_path = path+'/'+record
        data_list.append(load_data_pd_single_file(record_path))
    return data_list


if __name__ == '__main__':
    stime_pd = time.time()
    data_list_pd = load_data_pd('/home/lin/Documents/CAMH/SenseActivity/data/Test')
    etime_pd = time.time()
    print(len(data_list_pd[0]), len(data_list_pd[1]))
    print("The processing time for pandas is: " + str(etime_pd-stime_pd) + ' seconds.')
    