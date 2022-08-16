Implementation
==============

This page detailed the implementation for DQM metrics we are using in the sensor module as a supplementary material.
For the simpler definition of each metrics, please refer to the :doc:`glossary` page.

IRLR
  The ratio of the number of records having two or more data points over the total number of records, calculated as:
  :math:`IRLR = \frac{n(len>1)}{N}`, where :math:`n(len>1)` is the number of records having a length of 2 points and above,
  and :math:`N` is the total number of records.
  IRLR can be used to investigate a commonly observed quality issue that arises when the data collection app creates and uploads a record file that includes no data points or a single uninterpretable point.

SCR
  The ratio of available channels per record by the typical number of channels for each sensor, calculated as: 
  :math:`SCR = \frac{SCC}{ESCC}`, :math:`ESCC = mode(SCC)`, where :math:`SCC` is the sensor channel count, :math:`ESCC` is the expected sensor channel count calculated as the most frequent channel count per sensor.
  SCR allows the detection of missing channels (e.g., acceleration across the z-axis) in case of sensor defect or partial data upload.

MDR
  The ratio of missing data points over the total number of record points for all sensor types. 
  The MDR metric measures the level of discontinuity manifested through skipped data points due to undersampling, calculated as:
  :math:`MDR = \frac{MPC}{TPC}`, where :math:`MPC`` is the missing point count, and :math:`TPC` is the total point count.
  :math:`MPC += \frac{t(n+1)-t(n)}{\hat{t_{s}}} - 1`, :math:`if: t(n+1)-t(n) \geq 2\hat{t_{s}}`, and :math:`\hat{t_{s}} = mode(t_s)`. 
  Where :math:`t(n)` is the timestamp of point :math:`n`, :math:`t_s` is the sampling interval, and :math:`\hat{t_{s}` is the data-driven sampling interval calculated as the most frequent time interval.
  This type of data missingness quantifies the level of information loss, guiding the need for appropriate data resampling and interpolation methods. 

VDR
  The ratio of non-NaN data points over the total number of data points.
  The VDR metric measures the level of invalid data points in the records, calculated as:
  :math:`VDR = \frac{VPC}{TPC}`, where :math:`VPC`` is the valid point count, and :math:`TPC` is the total point count.
  :math:`VPC += 1,` if there is a non-NaN data point in the record.
  VDR allows the detection of NaN data points.

SNR
  A measure of the amplitude or power ratio of the signal component, i.e., desired data by the noise component.
  SNR describes the level of data variability around the mean absolute value,
  approximating the proportion of noise contamination with respect to the desired data of interest, calculated as:
  :math:`SNR = 20log\frac{S}{N} = 20log\frac{MAV(x)}{\sigma_{x}}`,
  where :math:`S` is the desired data (signal) approximated as the :math:`MAV` (mean absolute value) of data record :math:`x`,
  and :math:`N` is the undesired data (noise) approximated as the standard deviation of data record :math:`x`.
  This metric gives insight into the noise level rather than its type, providing feedback on the required level of data denoising. 

APD
  The ratio of anomalous points by the total number of recorded points, calculated as:
  :math:`APD = \frac{APC}{TPC}`, :math:`APC += 1, if: DS(x[n]) > \overline{DS(x)} + 3\sigma_{DS(x)}`,
  where :math:`APC` is the anomalous point count, and :math:`TPC` is the total point count.
  The :math:`APC` is incremented by 1 whenever the decision score (:math:`DS`) of a data sample :math:`x[n]` exceeds the set threshold being a z-score of 3.
  The APD metric allows for detecting and counting outliers in sensor data on a point-by-point basis, resulting in a density estimate of anomalies.
  It is computed using an unsupervised machine learning technique termed feature bagging method followed by outlier score thresholding to count anomalous points. 

RLC
  The inverse of the coefficient of variation of record length variability across data records, such that record length is the number of points per record. RLC is a measure of uniformity between the lengths of different data records across sensors, calculated as:
  :math:`RLC = 2(1 - sig(\frac{\sigma_{RL}}{\overline{RL}}))`
  where :math:`sig(x)` is the sigmoid function, :math:`\sigma_{RL}` is the standard deviation of record lengths, and :math:`\overline{RL}` is the mean record length. The higher RLC is, the less the burden of data segmentation and preprocessing is before the analysis. 

SRC
  The inverse of the coefficient of variation of the sampling intervals across sensors with the sampling interval as the difference between two consecutive data point timestamps, calculated as:
  :math:`SRC = 2(1 - sig(\frac{\sigma_{t_s}}{\overline{t_s}}))`, where :math:`sig(x)` is the sigmoid function, :math:`\sigma_{t_s}` is the standard deviation of sampling rates,
  and :math:`\overline{t_s}` is the mean sampling rate. SRC provides a measure of the stability of data discretization,
  hence the level of sampling continuity and uniformity. The higher SRC is, the less the risk of information loss is.

VRC
  The inverse of the coefficient of variation of record data value min-max range variability across sensors with the min-max range describing the difference between the maximum and minimum value of a record.
  VRC is the degree of stability of the data value range across sensors, calculated as: :math:`VRC = 2(1 - sig(\frac{\sigma_{VR}}{\overline{VR}}))`,
  where :math:`sig(x)` is the sigmoid function, :math:`\sigma_{VR}` is the standard deviation of value ranges, and :math:`\overline{VR}` is the mean value range.
  While value range variability is expected in real-world settings, high data consistency indicates low range variability, hence higher reproducibility and sensor output stability.

