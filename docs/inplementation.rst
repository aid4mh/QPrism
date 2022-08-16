Implementation
==============

This page detailed the implementation for DQM metrics we are using in the sensor module as a supplementary material.
For the simpler definition of each metrics, please refer to the :doc:`glossary` page.

IRLR
  | Inverse of the coefficient of variation of record length variability across data records, such that record length is the number of points per record.
  RLC is a measure of uniformity between the lengths of different data records across sensors, calculated as:
  | :math:`RLC = 2(1 - sig(\frac{\sigma_{RL}}{\bar{RL}}))`
  | where :math:`sig(x)` is the sigmoid function, :math:`\sigma_{RL}` is the standard deviation of record lengths, 
  and :math:`\bar{RL}` is the mean record length. The higher RLC is, the less the burden of data segmentation and preprocessing is before the analysis. 

