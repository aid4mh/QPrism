from QPrism.Sensor.DQM import DQM_multiple_record, DQM_single_record
from QPrism.Sensor.load_data import *
import pandas as pd


if __name__ == '__main__':
    
    # Compute DQM for an arbitrary json record located at data/sensor/json/ in the git repo
    single_file_dqm = DQM_single_record()
    # replace the path to your actual path locally
    df = load_data_json_single_file('path/to/the/json/record')
    single_file_dqm.set_input_data(df)
    single_file_dqm.compute_DQM()
    print(single_file_dqm.get_fields())
    print(single_file_dqm.get_DQM())

    # Compute DQM for an arbitrary csv record located at data/sensor/csv/ in the git repo
    single_csv_file_dqm = DQM_single_record()
    # replace the path to your actual path locally
    df = load_data_csv_one_file('path/to/the/csv/record')
    single_csv_file_dqm.set_input_data(df)
    single_csv_file_dqm.compute_DQM()
    print(single_csv_file_dqm.get_fields())
    print(single_csv_file_dqm.get_DQM())

    # Compute DQM for all the json records located at data/sensor/json in the git repo
    multi_file_dqm = DQM_multiple_record()
    # replace the path to your actual path locally
    df_list = load_data_json_multi_file('path/to/the/json/record/directory')
    multi_file_dqm.set_input_data(df_list)
    multi_file_dqm.compute_avg_DQM()
    print(multi_file_dqm.get_avg_fields())
    print(multi_file_dqm.get_avg_DQM())

    # Compute DQM for all the csv records located at data/sensor/csv in the git repo
    multi_csvfile_dqm = DQM_multiple_record()
    # replace the path to your actual path locally
    df_list = load_data_csv_multi_file('path/to/the/csv/record/directory')
    multi_csvfile_dqm.set_input_data(df_list)
    multi_csvfile_dqm.compute_DQM()
    print(multi_csvfile_dqm.get_fields())
    print(multi_csvfile_dqm.get_DQM())
