from DQM import DQM_multiple_file, DQM_single_file
from load_data import *
import pandas as pd


def load_sensor(path):
    records = os.listdir(path)
    filename_list = []
    MDR_list = []
    for record in records:
        record_path = path+'/'+record
        filename_list.append(record)
        df = load_data_json_single_file(record_path)
        single_file_DQM = DQM_single_file()
        single_file_DQM.set_APD(False)
        single_file_DQM.set_SCR(False)
        single_file_DQM.set_SNR(False)
        single_file_DQM.set_SRC(False)
        single_file_DQM.set_input_data(df)
        single_file_DQM.compute_DQM()
        MDR_list.append(single_file_DQM.get_MDR())
    return MDR_list, filename_list


def load_user(path):
    sensors = os.listdir(path)
    MDR_sensor_list = []
    filename_sensor_list = []
    for sensor in sensors:
        sensor_path = path+'/'+sensor
        MDR_list, filename_list = load_sensor(sensor_path)
        MDR_sensor_list.append(MDR_list)
        filename_sensor_list.append(filename_list)
    return filename_sensor_list, MDR_sensor_list


if __name__ == '__main__':
    print(load_user('/home/lin/Documents/CAMH/SenseActivity/data/Test/SUBJ00005'))
