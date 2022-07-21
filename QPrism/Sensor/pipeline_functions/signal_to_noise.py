import numpy as np
from scipy import *
from QPrism.Sensor.pipeline_functions.preprocessing import *

# def Signal_to_Noise(x):
#   n = len(x)
#   t = range(n)
#   signal = x
#   orders = range(5,40)
#   sse1 = np.zeros(len(orders))
#   np.savetxt('x.txt', x)
#   for ri in range(len(orders)):
#     yHat = np.polyval(polyfit(t,signal,orders[ri]),t)
#     sse1[ri] = np.sum( (yHat-signal)**2 )/n
#   # Bayes information criterion
#   bic = n*np.log(sse1) + orders*np.log(n)
#   # best parameter has lowest BIC
#   bestP = min(bic)
#   idx = np.argmin(bic)

#   ## now repeat filter for best (smallest) BIC
#   # polynomial fit
#   polycoefs = polyfit(t,signal,orders[idx])
#   # estimated data based on the coefficients
#   yHat = polyval(polycoefs,t)
#   # filtered signal is residual
#   filtsig = signal - yHat
#   SNR = 10*np.log10(np.mean(abs(filtsig))/np.mean(abs(yHat)))
#   return SNR
  
  
def Signal_to_Noise(arr):
    arr = arr[~np.isnan(arr)]
    arr = arr - np.mean(arr)
    arr = np.asarray(arr)
    abs = np.abs(arr)
    mean = abs.mean(axis=0)
    std_dev = arr.std(axis=0, ddof=1)
    snr = np.where(std_dev == 0, 0, mean/std_dev)
    return 20 * np.log10(snr)


def snr(record, feature_names):
    record = features_to_float(record, feature_names)
    #feat_values = [Signal_to_Noise([r[feature] for r in record]) for feature in feature_names]
    feat_values = []
    for feature in feature_names:
        feat_values.append(Signal_to_Noise(record[feature]))
    return np.mean([f for f in feat_values if not math.isnan(f)])