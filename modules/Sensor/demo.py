from DQM import DQM, DQM_single_file


if __name__ == '__main__':
    """dqm_obj = DQM()
    dqm_obj.set_input_path('/home/lin/Documents/CAMH/SenseActivity/data/Test')
    dqm_obj.set_APD(True)
    dqm_obj.set_MDR(True)
    dqm_obj.set_RLC(True)
    dqm_obj.set_SCR(True)
    dqm_obj.set_SNR(True)
    dqm_obj.set_SRC(True)
    dqm_obj.set_VRC(True)
    dqm_obj.compute_DQM()
    print(dqm_obj.get_DQM())
    print(dqm_obj.get_IRLR())
    print(dqm_obj.get_RLC())
    print(dqm_obj.get_SNR())
    print(dqm_obj.get_VRC())
    print(dqm_obj.get_SCR())
    print(dqm_obj.get_SRC())
    print(dqm_obj.get_MDR())
    print(dqm_obj.get_APD())"""
    #dqm_obj.save_to_file('/home/lin/Documents/CAMH/SenseActivity/data/result_extreme.csv')
    single_file_dqm = DQM_single_file()
    single_file_dqm.set_input_path('/home/lin/Documents/CAMH/SenseActivity/data/Test/SUBJ00001/Accelerometer/SUBJ00001_Accelerometer_REC000000.json')
    single_file_dqm.compute_DQM()
    print(single_file_dqm.get_IRLR())
