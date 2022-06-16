from load_data import *
from APD import compute_APD, compute_APD_multiple, compute_APD_single
from IRLR import compute_IRLR, compute_IRLR_multiple, compute_IRLR_single
from MDR import compute_MDR, compute_MDR_multiple, compute_MDR_single
from RLC import compute_RLC, compute_RLC_multiple_file
from SCR import compute_SCR, compute_SCR_multiple, compute_SCR_single
from SNR import compute_SNR, compute_SNR_multiple, compute_SNR_single
from SRC import compute_SRC, compute_SRC_multiple, compute_SRC_single
from VRC import compute_VRC, compute_VRC_multiple_file
import csv
import time
import numpy as np


class DQM:
    """
    A class represents the data quality matrix.
    """
    def __init__(self):
        self.input_path = None
        self.output_path = None
        self.user_score = []
        self.data_list_pd = None
        self.DQM_config = {'RLC': True, 'SNR': True, 'VRC': True,
                           'SCR': True, 'SRC': True, 'MDR': True, 'APD': True}
        self.DQM_function = {'RLC': compute_RLC,
                             'SNR': compute_SNR, 'VRC': compute_VRC,
                             'SCR': compute_SCR, 'SRC': compute_SRC,
                             'MDR': compute_MDR, 'APD': compute_APD}
        self.fields = ['userID', 'IRLR']
        self.stime = None
        self.loading_etime = None
        self.computing_etime = None
    
    def set_input_path(self, path:str):
        """
        Set the path of input folder.
        The folder should have the following structure:
            path\n
            │\n
            └───user1\n
            |  |\n
            |  └───sensor1\n
            |   |   |   record1.json\n
            |   |   |   record2.json\n
            |   |   |   ...\n
            |   └───sensor2\n
            |   |   |   record1.json\n
            |   |   |   record2.json\n
            |   |   |   ...\n
            |   |   ...\n
            └───user2\n
            |   |\n
            |   └───sensor1\n
            |   |   |   record1.json\n
            |   |   |   record2.json\n
            |   |   |   ...\n
            |   └───sensor2\n
            |   |   |   record1.json\n
            |   |   |   record2.json\n
            |   |   |   ...\n
            |   |   ...\n
            |   ...\n

        Parameters
        ----------
        path : str
            Path to the folder contains users' data. 
        """
        self.input_path = path
    
    def set_RLC(self, included:bool):
        """
        Set whether RLC is included as a metric

        Parameters
        ----------
        included : bool
            A bool value to indicate whether RLC is included in the result DQM
        """
        self.DQM_config['RLC'] = included
    
    def set_SNR(self, included:bool):
        """
        Set whether SNR is included as a metric

        Parameters
        ----------
        included : bool
            A bool value to indicate whether SNR is included in the result DQM
        """
        self.DQM_config['SNR'] = included
    
    def set_VRC(self, included:bool):
        """
        Set whether VRC is included as a metric

        Parameters
        ----------
        included : bool
            A bool value to indicate whether VRC is included in the result DQM
        """
        self.DQM_config['VRC'] = included
    
    def set_SCR(self, included:bool):
        """
        Set whether SCR is included as a metric

        Parameters
        ----------
        included : bool
            A bool value to indicate whether SCR is included in the result DQM
        """
        self.DQM_config['SCR'] = included
    
    def set_SRC(self, included:bool):
        """
        Set whether SRC is included as a metric

        Parameters
        ----------
        included : bool
            A bool value to indicate whether SRC is included in the result DQM
        """
        self.DQM_config['SRC'] = included
    
    def set_MDR(self, included:bool):
        """
        Set whether MDR is included as a metric

        Parameters
        ----------
        included : bool
            A bool value to indicate whether MDR is included in the result DQM
        """
        self.DQM_config['MDR'] = included
    
    def set_APD(self, included:bool):
        """
        Set whether APD is included as a metric

        Parameters
        ----------
        included : bool
            A bool value to indicate whether APD is included in the result DQM
        """
        self.DQM_config['APD'] = included
    
    def compute_DQM(self):
        """
        Compute the DQMs for current configuration.
        Must call set_input_path before calling this method.
        """
        self.stime = time.time()
        print("Loading data...")
        self.data_list_pd = load_data_pd(self.input_path)
        self.loading_etime = time.time()
        print("The total time for loading data into dataframe is: " + str(self.loading_etime-self.stime) + ' seconds.')
        print("Start computing the DQM... This may take a long time if the dataset is large")
        for key in self.DQM_config.keys():
                if self.DQM_config[key] is True:
                    self.fields.append(key)
        for i in range (len(self.data_list_pd[1])):
            self.user_score.append([])
            self.user_score[i].append(str(self.data_list_pd[0][i]))
            # exclude current user from analysis if the user has no sufficient record
            self.user_score[i].append(str(compute_IRLR(self.data_list_pd[1][i])))
            if (float(self.user_score[i][-1])!=0):
                for key in self.DQM_config.keys():
                    if self.DQM_config[key] is True:
                        self.user_score[i].append(str(self.DQM_function[key](self.data_list_pd[1][i])))
            else:
                for key in self.DQM_config.keys():
                    if self.DQM_config[key] is True:
                        self.user_score[i].append(np.NAN)
        self.computing_etime = time.time()
        print("The total time for computing the DQM is: " + str(self.computing_etime-self.stime) + ' seconds.')
    
    def get_DQM(self):
        """
        Return the computed DQM as a list. compute_DQM must be called before this method.
        """
        return self.user_score
    
    def get_fields(self):
        """
        Return a list represents the current included info in DQM.
        compute_DQM must be called before this method.
        """
        return self.fields

    def get_IRLR(self):
        """
        Return the IRLR score for given input data as a dict {user_ID: user_IRLR}.
        IRLR must be included in the DQM class.
        """
        IRLR_dict = {}
        for user in self.user_score:
            IRLR_dict[user[0]] = user[1]
        return IRLR_dict
    
    def get_RLC(self):
        """
        Return the RLC score for given input data as a dict {user_ID: user_RLC}.
        RLC must be included in the DQM class.
        """
        RLC_dict = {}
        RLC_index = self.fields.index('RLC')
        if (RLC_index==-1):
            return RLC_dict
        for user in self.user_score:
            RLC_dict[user[0]] = user[RLC_index]
        return RLC_dict
    
    def get_SNR(self):
        """
        Return the SNR score for given input data as a dict {user_ID: user_SNR}.
        SNR must be included in the DQM class.
        """
        SNR_dict = {}
        SNR_index = self.fields.index('SNR')
        if (SNR_index==-1):
            return SNR_dict
        for user in self.user_score:
            SNR_dict[user[0]] = user[SNR_index]
        return SNR_dict
    
    def get_VRC(self):
        """
        Return the VRC score for given input data as a dict {user_ID: user_VRC}.
        VRC must be included in the DQM class.
        """
        VRC_dict = {}
        VRC_index = self.fields.index('VRC')
        if (VRC_index==-1):
            return VRC_dict
        for user in self.user_score:
            VRC_dict[user[0]] = user[VRC_index]
        return VRC_dict
    
    def get_SCR(self):
        """
        Return the SCR score for given input data as a dict {user_ID: user_SCR}.
        SCR must be included in the DQM class.
        """
        SCR_dict = {}
        SCR_index = self.fields.index('SCR')
        if (SCR_index==-1):
            return SCR_dict
        for user in self.user_score:
            SCR_dict[user[0]] = user[SCR_index]
        return SCR_dict
    
    def get_SRC(self):
        """
        Return the SRC score for given input data as a dict {user_ID: user_SRC}.
        SRC must be included in the DQM class.
        """
        SRC_dict = {}
        SRC_index = self.fields.index('SRC')
        if (SRC_index==-1):
            return SRC_dict
        for user in self.user_score:
            SRC_dict[user[0]] = user[SRC_index]
        return SRC_dict
    
    def get_MDR(self):
        """
        Return the MDR score for given input data as a dict {user_ID: user_MDR}.
        MDR must be included in the DQM class.
        """
        MDR_dict = {}
        MDR_index = self.fields.index('MDR')
        if (MDR_index==-1):
            return MDR_dict
        for user in self.user_score:
            MDR_dict[user[0]] = user[MDR_index]
        return MDR_dict
    
    def get_APD(self):
        """
        Return the APD score for given input data as a dict {user_ID: user_APD}.
        APD must be included in the DQM class.
        """
        APD_dict = {}
        APD_index = self.fields.index('APD')
        if (APD_index==-1):
            return APD_dict
        for user in self.user_score:
            APD_dict[user[0]] = user[APD_index]
        return APD_dict
    
    def save_to_file(self, path:str):
        """
        Save the computed DQMs as a csv file to the set output path.
        Must call set_output_path and compute DQMs before calling this.

        Parameters
        ----------
        path : str
            Path to the result file
        
        """
        self.output_path = path
        with open(self.output_path, 'w') as result_file:
            write = csv.writer(result_file)
            write.writerow(self.fields)
            write.writerows(self.user_score)
        print("Data successfuly saved.")


class DQM_single_file:
    """
    A class represents the data quality matrix.
    """
    def __init__(self):
        self.input_path = None
        self.output_path = None
        self.score = []
        self.data_list_pd = None
        self.DQM_config = {'SNR': True, 'SCR': True,
                           'SRC': True, 'MDR': True, 'APD': True}
        self.DQM_function = {'SNR': compute_SNR_single,
                             'SCR': compute_SCR_single, 'SRC': compute_SRC_single,
                             'MDR': compute_MDR_single, 'APD': compute_APD_single}
        self.fields = ['IRLR']
        self.stime = None
        self.loading_etime = None
        self.computing_etime = None
    
    def set_input_path(self, path:str):
        """
        Set the path of input file.
        """
        self.input_path = path
    
    def set_RLC(self, included:bool):
        """
        Set whether RLC is included as a metric

        Parameters
        ----------
        included : bool
            A bool value to indicate whether RLC is included in the result DQM
        """
        self.DQM_config['RLC'] = included
    
    def set_SNR(self, included:bool):
        """
        Set whether SNR is included as a metric

        Parameters
        ----------
        included : bool
            A bool value to indicate whether SNR is included in the result DQM
        """
        self.DQM_config['SNR'] = included
    
    def set_VRC(self, included:bool):
        """
        Set whether VRC is included as a metric

        Parameters
        ----------
        included : bool
            A bool value to indicate whether VRC is included in the result DQM
        """
        self.DQM_config['VRC'] = included
    
    def set_SCR(self, included:bool):
        """
        Set whether SCR is included as a metric

        Parameters
        ----------
        included : bool
            A bool value to indicate whether SCR is included in the result DQM
        """
        self.DQM_config['SCR'] = included
    
    def set_SRC(self, included:bool):
        """
        Set whether SRC is included as a metric

        Parameters
        ----------
        included : bool
            A bool value to indicate whether SRC is included in the result DQM
        """
        self.DQM_config['SRC'] = included
    
    def set_MDR(self, included:bool):
        """
        Set whether MDR is included as a metric

        Parameters
        ----------
        included : bool
            A bool value to indicate whether MDR is included in the result DQM
        """
        self.DQM_config['MDR'] = included
    
    def set_APD(self, included:bool):
        """
        Set whether APD is included as a metric

        Parameters
        ----------
        included : bool
            A bool value to indicate whether APD is included in the result DQM
        """
        self.DQM_config['APD'] = included
    
    def compute_DQM(self):
        """
        Compute the DQMs for current configuration.
        Must call set_input_path before calling this method.
        """
        self.score = []
        self.fields = ['IRLR']
        self.stime = time.time()
        print("Loading data...")
        self.data_list_pd = load_data_pd_single_file(self.input_path)
        self.loading_etime = time.time()
        print("The total time for loading data into dataframe is: " + str(self.loading_etime-self.stime) + ' seconds.')
        print("Start computing the DQM... This may take a long time if the dataset is large")
        for key in self.DQM_config.keys():
                if self.DQM_config[key] is True:
                    self.fields.append(key)
        self.score.append(str(compute_IRLR_single(self.data_list_pd)))
        if (float(self.score[-1])!=0):
            for key in self.DQM_config.keys():
                if self.DQM_config[key] is True:
                    self.score.append(str(self.DQM_function[key](self.data_list_pd)))
        else:
            for key in self.DQM_config.keys():
                if self.DQM_config[key] is True:
                    self.score.append(np.NAN)
        self.computing_etime = time.time()
        print("The total time for computing the DQM is: " + str(self.computing_etime-self.stime) + ' seconds.')
    
    def get_DQM(self):
        """
        Return the computed DQM as a list. compute_DQM must be called before this method.
        """
        return self.score
    
    def get_fields(self):
        """
        Return a list represents the current included info in DQM.
        compute_DQM must be called before this method.
        """
        return self.fields

    def get_IRLR(self):
        """
        Return the IRLR score for given input data as a dict {user_ID: user_IRLR}.
        IRLR must be included in the DQM class.
        """
        IRLR_index = self.fields.index('IRLR')
        return self.score[IRLR_index]
    
    def get_SNR(self):
        """
        Return the SNR score for given input data as a dict {user_ID: user_SNR}.
        SNR must be included in the DQM class.
        """
        SNR_index = self.fields.index('SNR')
        if (SNR_index==-1):
            return "Not computed"
        return self.score[SNR_index]
    
    def get_SCR(self):
        """
        Return the SCR score for given input data as a dict {user_ID: user_SCR}.
        SCR must be included in the DQM class.
        """
        SCR_index = self.fields.index('SCR')
        if (SCR_index==-1):
            return "Not computed"
        return self.score[SCR_index]
    
    def get_SRC(self):
        """
        Return the SRC score for given input data as a dict {user_ID: user_SRC}.
        SRC must be included in the DQM class.
        """
        SRC_index = self.fields.index('SRC')
        if (SRC_index==-1):
            return "Not computed"
        return self.score[SRC_index]
    
    def get_MDR(self):
        """
        Return the MDR score for given input data as a dict {user_ID: user_MDR}.
        MDR must be included in the DQM class.
        """
        MDR_index = self.fields.index('MDR')
        if (MDR_index==-1):
            return "Not computed"
        return self.score[MDR_index]
    
    def get_APD(self):
        """
        Return the APD score for given input data as a dict {user_ID: user_APD}.
        APD must be included in the DQM class.
        """
        APD_index = self.fields.index('APD')
        if (APD_index==-1):
            return "Not computed"
        return self.score[APD_index]
    
    def save_to_file(self, path:str):
        """
        Save the computed DQMs as a csv file to the set output path.
        Must call set_output_path and compute DQMs before calling this.

        Parameters
        ----------
        path : str
            Path to the result file
        
        """
        self.output_path = path
        with open(self.output_path, 'w') as result_file:
            write = csv.writer(result_file)
            write.writerow(self.fields)
            write.writerow(self.score)
        print("Data successfuly saved.")


class DQM_multiple_file:
    """
    A class represents the data quality matrix for multiple files in one directory.
    """
    def __init__(self):
        self.input_path = None
        self.output_path = None
        self.score = []
        self.data_list = None
        self.DQM_config = {'SNR': True, 'SCR': True, 'RLC': True, 'VRC': True,
                           'SRC': True, 'MDR': True, 'APD': True}
        self.DQM_function = {'SNR': compute_SNR_multiple, 'RLC': compute_RLC_multiple_file,
                             'SCR': compute_SCR_multiple, 'SRC': compute_SRC_multiple, 'VRC': compute_VRC_multiple_file, 
                             'MDR': compute_MDR_multiple, 'APD': compute_APD_multiple}
        self.fields = ['IRLR']
        self.stime = None
        self.loading_etime = None
        self.computing_etime = None
    
    def set_input_path(self, path:str):
        """
        Set the path of input file.
        """
        self.input_path = path
    
    def set_RLC(self, included:bool):
        """
        Set whether RLC is included as a metric

        Parameters
        ----------
        included : bool
            A bool value to indicate whether RLC is included in the result DQM
        """
        self.DQM_config['RLC'] = included
    
    def set_SNR(self, included:bool):
        """
        Set whether SNR is included as a metric

        Parameters
        ----------
        included : bool
            A bool value to indicate whether SNR is included in the result DQM
        """
        self.DQM_config['SNR'] = included
    
    def set_VRC(self, included:bool):
        """
        Set whether VRC is included as a metric

        Parameters
        ----------
        included : bool
            A bool value to indicate whether VRC is included in the result DQM
        """
        self.DQM_config['VRC'] = included
    
    def set_SCR(self, included:bool):
        """
        Set whether SCR is included as a metric

        Parameters
        ----------
        included : bool
            A bool value to indicate whether SCR is included in the result DQM
        """
        self.DQM_config['SCR'] = included
    
    def set_SRC(self, included:bool):
        """
        Set whether SRC is included as a metric

        Parameters
        ----------
        included : bool
            A bool value to indicate whether SRC is included in the result DQM
        """
        self.DQM_config['SRC'] = included
    
    def set_MDR(self, included:bool):
        """
        Set whether MDR is included as a metric

        Parameters
        ----------
        included : bool
            A bool value to indicate whether MDR is included in the result DQM
        """
        self.DQM_config['MDR'] = included
    
    def set_APD(self, included:bool):
        """
        Set whether APD is included as a metric

        Parameters
        ----------
        included : bool
            A bool value to indicate whether APD is included in the result DQM
        """
        self.DQM_config['APD'] = included
    
    def compute_DQM(self):
        """
        Compute the DQMs for current configuration.
        Must call set_input_path before calling this method.
        """
        self.score = []
        self.fields = ['IRLR']
        self.stime = time.time()
        print("Loading data...")
        self.data_list = load_data_pd_multi_file(self.input_path)
        self.loading_etime = time.time()
        print("The total time for loading data into dataframe is: " + str(self.loading_etime-self.stime) + ' seconds.')
        print("Start computing the DQM... This may take a long time if the dataset is large")
        for key in self.DQM_config.keys():
                if self.DQM_config[key] is True:
                    self.fields.append(key)
        self.score.append(str(compute_IRLR_multiple(self.data_list)))
        if (float(self.score[-1])!=0):
            for key in self.DQM_config.keys():
                if self.DQM_config[key] is True:
                    self.score.append(str(self.DQM_function[key](self.data_list)))
        else:
            for key in self.DQM_config.keys():
                if self.DQM_config[key] is True:
                    self.score.append(np.NAN)
        self.computing_etime = time.time()
        print("The total time for computing the DQM is: " + str(self.computing_etime-self.stime) + ' seconds.')
    
    def get_DQM(self):
        """
        Return the computed DQM as a list. compute_DQM must be called before this method.
        """
        return self.score
    
    def get_fields(self):
        """
        Return a list represents the current included info in DQM.
        compute_DQM must be called before this method.
        """
        return self.fields

    def get_IRLR(self):
        """
        Return the IRLR score for given input data as a dict {user_ID: user_IRLR}.
        IRLR must be included in the DQM class.
        """
        IRLR_index = self.fields.index('IRLR')
        return self.score[IRLR_index]
    
    def get_SNR(self):
        """
        Return the SNR score for given input data as a dict {user_ID: user_SNR}.
        SNR must be included in the DQM class.
        """
        SNR_index = self.fields.index('SNR')
        if (SNR_index==-1):
            return "Not computed"
        return self.score[SNR_index]
    
    def get_SCR(self):
        """
        Return the SCR score for given input data as a dict {user_ID: user_SCR}.
        SCR must be included in the DQM class.
        """
        SCR_index = self.fields.index('SCR')
        if (SCR_index==-1):
            return "Not computed"
        return self.score[SCR_index]
    
    def get_SRC(self):
        """
        Return the SRC score for given input data as a dict {user_ID: user_SRC}.
        SRC must be included in the DQM class.
        """
        SRC_index = self.fields.index('SRC')
        if (SRC_index==-1):
            return "Not computed"
        return self.score[SRC_index]
    
    def get_MDR(self):
        """
        Return the MDR score for given input data as a dict {user_ID: user_MDR}.
        MDR must be included in the DQM class.
        """
        MDR_index = self.fields.index('MDR')
        if (MDR_index==-1):
            return "Not computed"
        return self.score[MDR_index]
    
    def get_APD(self):
        """
        Return the APD score for given input data as a dict {user_ID: user_APD}.
        APD must be included in the DQM class.
        """
        APD_index = self.fields.index('APD')
        if (APD_index==-1):
            return "Not computed"
        return self.score[APD_index]
    
    def get_RLC(self):
        """
        Return the RLC score for given input data as a dict {user_ID: user_APD}.
        RLC must be included in the DQM class.
        """
        RLC_index = self.fields.index('RLC')
        if (RLC_index==-1):
            return "Not computed"
        return self.score[RLC_index]
    
    def get_VRC(self):
        """
        Return the VRC score for given input data as a dict {user_ID: user_VRC}.
        VRC must be included in the DQM class.
        """
        VRC_index = self.fields.index('VRC')
        if (VRC_index==-1):
            return "Not computed"
        return self.score[VRC_index]
    
    def save_to_file(self, path:str):
        """
        Save the computed DQMs as a csv file to the set output path.
        Must call set_output_path and compute DQMs before calling this.

        Parameters
        ----------
        path : str
            Path to the result file
        
        """
        self.output_path = path
        with open(self.output_path, 'w') as result_file:
            write = csv.writer(result_file)
            write.writerow(self.fields)
            write.writerow(self.score)
        print("Data successfuly saved.")