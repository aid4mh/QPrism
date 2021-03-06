Glossary
========

Audio Module
------------

word
  explanation


Video Module
------------

word
  explanation

word
  explanation

Sensor Module
-------------

DQM
  Data Quality Matrix. The matrix generated by the pipeline, including all the quality assessment metrics
  that are related to user's research.

Correctness
  One of the three aspects that the pipeline evaluates. It measures the overall correctness of the input data
  via APD and SNR.

Completeness
  One of the three aspects that the pipeline evaluates. It measures the overall completeness of the input data
  via IRLR, MDR, SCR, and VDR.

Consistency
  One of the three aspects that the pipeline evaluates. It measures the overall consistency of the input data
  via RLC, SRC, and VRC.

APD
  Anomalous Points Density. The ratio of the number of outliers/anomalous data samples by the total number of samples.

IRLR
  Interpretable Record Length Ratio. The ratio of the number of interpretable records by the total number of records.
  A record is interpretable if it satisfies the following: 
  a. Has more than one row of data. 
  b. Has non-decreasing timestamp.
  c. Has non-zero standard deviation on each data channel.

MDR
  Missing Data Ratio. The ratio of the number of missing data samples by the total number of samples. TBD

RLC
  Record Length Consistency. The uniformness of data record length across multiple records.

SCR
  Sensor Channel Ratio. The ratio of the number of records that has full channels by the total number of records.
  A record is defined to have full channels if the number of its channels is the same as the mode of the number of channels
  of given input. 

SNR
  Signal-to-noise Ratio. The ratio of desired signal amplitude by the noise amplitude.

SRC
  Sampling Rate Consistency. The uniformness of the data sampling rate within a record.

VRC
  Value Range Consistency. The uniformness of the value range across multiple records.

VDR
  Valid Data Ratio. The ratio of the number of non-NaN data points by the total number of data points. 