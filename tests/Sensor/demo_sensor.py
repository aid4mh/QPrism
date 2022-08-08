from QPrism.Sensor.DQM import DQM_multiple_file, DQM_single_file
from QPrism.Sensor.load_data import *
import pandas as pd


if __name__ == '__main__':
    #dqm_obj.save_to_file('/home/lin/Documents/CAMH/SenseActivity/data/result_extreme.csv')
    single_file_dqm = DQM_single_file()
    df = load_data_json_single_file('/home/lin/Documents/CAMH/SenseActivity/data/Test/SUBJ00001/Accelerometer/SUBJ00001_Accelerometer_REC000000.json')
    single_file_dqm.set_input_data(df)
    single_file_dqm.compute_DQM()
    print(single_file_dqm.get_fields())
    print(single_file_dqm.get_DQM())
    single_csv_file_dqm = DQM_single_file()
    df = load_data_csv_one_file('/home/lin/Documents/CAMH/SenseActivity/data/csv_data/id9603e9c3.csv')
    single_csv_file_dqm.set_input_data(df)
    single_csv_file_dqm.compute_DQM()
    print(single_csv_file_dqm.get_fields())
    print(single_csv_file_dqm.get_DQM())
    multi_file_dqm = DQM_multiple_file()
    df_list = load_data_json_multi_file('/home/lin/Documents/CAMH/SenseActivity/data/Test/SUBJ00001/Accelerometer')
    multi_file_dqm.set_input_data(df_list)
    multi_file_dqm.compute_avg_DQM()
    print(multi_file_dqm.get_avg_fields())
    print(multi_file_dqm.get_avg_DQM())
    """multi_csvfile_dqm = DQM_multiple_file()
    df_list = load_data_csv_multi_file('/home/lin/Documents/CAMH/SenseActivity/data/csv_data')
    multi_csvfile_dqm.set_input_data(df_list)
    multi_csvfile_dqm.compute_DQM()
    print(multi_csvfile_dqm.get_fields())
    print(multi_csvfile_dqm.get_DQM())"""
    """single_file_dqm = DQM_single_file()
    df = load_data_json_single_file('/home/lin/Documents/CAMH/SenseActivity/data/Test/SUBJ00008/GPS/SUBJ00008_GPS_REC000000.json')
    single_file_dqm.set_input_data(df)
    single_file_dqm.compute_DQM()
    print(single_file_dqm.get_fields())
    print(single_file_dqm.get_DQM())"""
