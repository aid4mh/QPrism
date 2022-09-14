from QPrism.Sensor.load_data import *
from QPrism.Sensor.APD import compute_APD_multiple, compute_APD_single
from QPrism.Sensor.IRLR import compute_IRLR_multiple, compute_IRLR_single
from QPrism.Sensor.MDR import compute_MDR_multiple, compute_MDR_single
from QPrism.Sensor.RLC import compute_RLC_multiple_file
from QPrism.Sensor.SCR import compute_SCR_multiple
from QPrism.Sensor.SNR import compute_SNR_multiple, compute_SNR_single
from QPrism.Sensor.SRC import compute_SRC_multiple, compute_SRC_single
from QPrism.Sensor.VRC import compute_VRC_multiple_file
from QPrism.Sensor.VDR import compute_VDR_single, compute_VDR_multiple
import QPrism.Sensor.APD as APD
import csv
import time
import numpy as np


class DQM_single_record:
    """
    A class represents the data quality matrix.
    """
    def __init__(self):
        self.output_path = None
        self.score = []
        self.data_list_pd = None
        self.DQM_config = {'SNR': True, 'VDR': True,
                           'SRC': True, 'MDR': True, 'APD': True}
        self.DQM_function = {'SNR': compute_SNR_single, 'VDR': compute_VDR_single,
                             'SRC': compute_SRC_single,
                             'MDR': compute_MDR_single, 'APD': compute_APD_single}
        self.fields = ['IRLR']
        self.stime = None
        self.loading_etime = None
        self.computing_etime = None
    
    def set_input_data(self, df:pd.DataFrame):
        """
        Set the path of input record file.

        Parameters
        ----------
        path : str
            Path to the input record file
        """
        self.data_list_pd = df
    
    def set_SNR(self, included:bool):
        """
        Set whether SNR is included as a metric

        Parameters
        ----------
        included : bool
            A bool value to indicate whether SNR is included in the result DQM
        """
        self.DQM_config['SNR'] = included
    
    def set_VDR(self, included:bool):
        """
        Set whether VDR is included as a metric

        Parameters
        ----------
        included : bool
            A bool value to indicate whether VDR is included in the result DQM
        """
        self.DQM_config['VDR'] = included
    
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
        Compute the DQM for input record under current metrics configuration.
        Must call set_input_path before calling this method.
        """
        self.score = []
        self.fields = ['IRLR']
        self.stime = time.time()
        # You can remove the comment below to print the computation time. Note this will cause compute_individual_DQM in 
        # the DQM_multi_file class to print this info for each record.
        #print("Start computing the DQM... This may take a long time if the dataset is large")
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
        self.etime = time.time()
        #print("The total time for computing the DQM is: " + str(self.etime-self.stime) + ' seconds.')
    
    def get_DQM(self):
        """
        Return the computed DQM as a list. compute_DQM must be called before this method.
        """
        return self.score
    
    def get_fields(self):
        """
        Return a list represents the current included metrics in DQM.
        compute_DQM must be called before this method.
        """
        return self.fields

    def get_IRLR(self):
        """
        Return the IRLR score for given input data as str.
        """
        IRLR_index = self.fields.index('IRLR')
        return self.score[IRLR_index]
    
    def get_SNR(self):
        """
        Return the SNR score for given input data as a str.
        SNR must be included in the DQM class.
        """
        try:
            SNR_index = self.fields.index('SNR')
        except ValueError:
            return "SNR is not computed according to the configuration"
        return self.score[SNR_index]
    
    def get_VDR(self):
        """
        Return the VDR score for given input data as a str.
        VDR must be included in the DQM class.
        """
        try:
            VDR_index = self.fields.index('VDR')
        except ValueError:
            return "VDR is not computed according to the configuration"
        return self.score[VDR_index]
    
    def get_SRC(self):
        """
        Return the SRC score for given input data as a str.
        SRC must be included in the DQM class.
        """
        try:
            SRC_index = self.fields.index('SRC')
        except ValueError:
            return "SRC is not computed according to the configuration"
        return self.score[SRC_index]
    
    def get_MDR(self):
        """
        Return the MDR score for given input data as a str.
        MDR must be included in the DQM class.
        """
        try:
            MDR_index = self.fields.index('MDR')
        except ValueError:
            return "MDR is not computed according to the configuration"
        return self.score[MDR_index]
    
    def get_APD(self):
        """
        Return the APD score for given input data as a str.
        APD must be included in the DQM class.
        """
        try:
            APD_index = self.fields.index('APD')
        except ValueError:
            return "APD is not computed according to the configuration"
        return self.score[APD_index]
    
    def get_anomaly_index(self):
        """
        Return the index (row number) of the anamoly points for the input record.
        APD must be included in the DQM class.
        """ 
        return APD.outlier_index
    
    def save_to_file(self, path:str):
        """
        Save the computed DQM as a csv file to the given output path.
        Must call compute_DQM before calling this.

        Parameters
        ----------
        path : str
            Path to the output file
        
        """
        self.output_path = path
        with open(self.output_path, 'w') as result_file:
            write = csv.writer(result_file)
            write.writerow(self.fields)
            write.writerow(self.score)
        print("Data successfuly saved.")


class DQM_multiple_record:
    """
    A class represents the data quality matrix for multiple files in one directory.
    """
    def __init__(self):
        self.output_path = None
        self.score = []
        self.individual_score = []
        self.data_list = None
        self.DQM_config = {'SNR': True, 'SCR': True, 'RLC': True, 'VRC': True,
                           'SRC': True, 'MDR': True, 'APD': True, 'VDR': True}
        self.DQM_function = {'SNR': compute_SNR_multiple, 'RLC': compute_RLC_multiple_file,
                             'SCR': compute_SCR_multiple, 'SRC': compute_SRC_multiple, 'VRC': compute_VRC_multiple_file, 
                             'MDR': compute_MDR_multiple, 'APD': compute_APD_multiple, 'VDR': compute_VDR_multiple}
        self.fields = ['IRLR']
        self.individual_fields = ['IRLR']
        self.stime = None
        self.loading_etime = None
        self.computing_etime = None
    
    def set_input_data(self, df_list):
        """
        Set the input data list of input file.

        Parameters
        ----------
        df_list : list of pd.DataFrame
            A list of dataframe, each dataframe represents a single record
        """
        self.data_list = df_list
    
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
    
    def set_VDR(self, included:bool):
        """
        Set whether VDR is included as a metric

        Parameters
        ----------
        included : bool
            A bool value to indicate whether VDR is included in the result DQM
        """
        self.DQM_config['VDR'] = included
    
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
    
    def compute_avg_DQM(self):
        """
        Compute a DQM for the input records under current metrics configuration.
        The DQM averaged all the metrics that are supported in DQM_single_file.
        In addition to above metrics, it also computes all the metrics only support DQM_multi_file.
        The computed DQM consists only one row. If you wish to get the DQM for each individual record,
        call the compute_individual_DQM method instead.
        Must call set_input_path before calling this method.
        """
        self.score = []
        self.fields = ['IRLR']
        self.stime = time.time()
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
        self.etime = time.time()
        print("The total time for computing the DQM is: " + str(self.etime-self.stime) + ' seconds.')
    
    def compute_individual_DQM(self):
        """
        Compute a DQM for the input records under current metrics configuration.
        This computes the DQM for each individual record, and store the DQMs as a list.
        If you wish to get the averaged DQM with the metrics only support multiple records,
        call the compute_avg_DQM method instead.
        Must call set_input_path before calling this method.
        """
        self.individual_score = []
        self.individual_fields = ['IRLR']
        self.stime = time.time()
        print("Start computing the DQM... This may take a long time if the dataset is large")
        multi_metrics_only = ['VRC', 'SCR', 'RLC']
        single_metrics = ['SNR', 'VDR', 'SRC', 'MDR', 'APD']
        for key in self.DQM_config.keys():
                if self.DQM_config[key] is True:
                    if key not in multi_metrics_only:
                        self.individual_fields.append(key)
        for record in self.data_list:
            single_DQM = DQM_single_record()
            single_DQM.set_input_data(record)
            for key in single_metrics:
                if key not in self.individual_fields:
                    if key=='SNR':
                        single_DQM.set_SNR(False)
                    elif key=='VDR':
                        single_DQM.set_VDR(False)
                    elif key=='SRC':
                        single_DQM.set_SRC(False)
                    elif key=='MDR':
                        single_DQM.set_MDR(False)
                    elif key=='APD':
                        single_DQM.set_APD(False)
            single_DQM.compute_DQM()
            single_result = []
            for key in self.individual_fields:
                if key=='IRLR':
                    single_result.append(single_DQM.get_IRLR())
                if key=='SNR':
                    single_result.append(single_DQM.get_SNR())
                if key=='VDR':
                    single_result.append(single_DQM.get_VDR())
                if key=='SRC':
                    single_result.append(single_DQM.get_SRC())
                if key=='MDR':
                    single_result.append(single_DQM.get_MDR())
                if key=='APD':
                    single_result.append(single_DQM.get_APD())
            self.individual_score.append(single_result)
        self.etime = time.time()
        print("The total time for computing the DQM is: " + str(self.etime-self.stime) + ' seconds.')
    
    def get_avg_DQM(self):
        """
        Return the computed DQM as a list. compute_DQM must be called before this method.
        """
        return self.score
    
    def get_individual_DQM(self):
        """
        Return the computed individual DQM as a list. Each element in the list represents a single record.
        compute_individual DQM must be called before this method.
        """
        return self.individual_score
    
    def get_avg_fields(self):
        """
        Return a list represents the current included metrics in the multi-file DQM.
        compute_avg_DQM must be called before this method.
        """
        return self.fields
    
    def get_individual_fields(self):
        """
        Return a list represents the current included metrics in the individual file DQM.
        compute_individual_DQM must be called before this method.
        """
        return self.individual_fields

    def get_IRLR(self):
        """
        Return the IRLR score for given input data as a str.
        """
        IRLR_index = self.fields.index('IRLR')
        return self.score[IRLR_index]
    
    def get_SNR(self):
        """
        Return the SNR score for given input data as a str.
        SNR must be included in the DQM class.
        """
        try:
            SNR_index = self.fields.index('SNR')
        except ValueError:
            return "SNR is not computed according to the configuration"
        return self.score[SNR_index]
    
    def get_VDR(self):
        """
        Return the VDR score for given input data as a str.
        VDR must be included in the DQM class.
        """
        try:
            VDR_index = self.fields.index('VDR')
        except ValueError:
            return "VDR is not computed according to the configuration"
        return self.score[VDR_index]
    
    def get_SCR(self):
        """
        Return the SCR score for given input data as a str.
        SCR must be included in the DQM class.
        """
        try:
            SCR_index = self.fields.index('SCR')
        except ValueError:
            return "SCR is not computed according to the configuration"
        return self.score[SCR_index]
    
    def get_SRC(self):
        """
        Return the SRC score for given input data as a str.
        SRC must be included in the DQM class.
        """
        try:
            SRC_index = self.fields.index('SRC')
        except ValueError:
            return "SRC is not computed according to the configuration"
        return self.score[SRC_index]
    
    def get_MDR(self):
        """
        Return the MDR score for given input data as a str.
        MDR must be included in the DQM class.
        """
        try:
            MDR_index = self.fields.index('MDR')
        except ValueError:
            return "MDR is not computed according to the configuration"
        return self.score[MDR_index]
    
    def get_APD(self):
        """
        Return the APD score for given input data as a str.
        APD must be included in the DQM class.
        """
        try:
            APD_index = self.fields.index('APD')
        except ValueError:
            return "APD is not computed according to the configuration"
        return self.score[APD_index]
    
    def get_RLC(self):
        """
        Return the RLC score for given input data as a str.
        RLC must be included in the DQM class.
        """
        try:
            RLC_index = self.fields.index('RLC')
        except ValueError:
            return "RLC is not computed according to the configuration"
        return self.score[RLC_index]
    
    def get_VRC(self):
        """
        Return the VRC score for given input data as a str.
        VRC must be included in the DQM class.
        """
        try:
            VRC_index = self.fields.index('VRC')
        except ValueError:
            return "VRC is not computed according to the configuration"
        return self.score[VRC_index]
    
    def save_avg_DQM_to_file(self, path:str):
        """
        Save the computed DQM as a csv file to the given output path.
        Must call compute_DQM before calling this.

        Parameters
        ----------
        path : str
            Path to the output file
        
        """
        self.output_path = path
        with open(self.output_path, 'w') as result_file:
            write = csv.writer(result_file)
            write.writerow(self.fields)
            write.writerow(self.score)
        print("Data successfuly saved.")
    
    def save_individual_DQM_to_file(self, path:str):
        """
        Save the computed DQM as a csv file to the given output path.
        Must call compute_DQM before calling this.

        Parameters
        ----------
        path : str
            Path to the output file
        
        """
        self.output_path = path
        with open(self.output_path, 'w') as result_file:
            write = csv.writer(result_file)
            write.writerow(self.individual_fields)
            for individual_DQM in self.individual_score:
                write.writerow(individual_DQM)
        print("Data successfuly saved.")