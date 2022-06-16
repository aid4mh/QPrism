import numpy as np
import scipy.stats as stats
from collections import Counter
import math
from pipeline_functions.preprocessing import *


def sigmoid(x):
    return 1/(1 + np.exp(-x))


def consistency(data):
    data = np.asanyarray(data)
    co_var = abs(stats.variation(data, nan_policy='omit'))
    if math.isnan(co_var):
        co_var = 0
    consis = (1 - sigmoid(co_var))*2
    return consis
    #return 1/co_var if co_var != 0 else np.inf


def mode(vals):
    return Counter(vals).most_common(1)[0][0]


def channel_completeness(record, feature_names):
    record = features_to_float(record, feature_names)
    channel = [len([r[feature] for r in record]) for feature in feature_names]
    return 1 if min(channel) == max(channel) else 0


def minmax(record, feature_names):
    record = features_to_float(record, feature_names)
    return np.mean([np.max([r[feature] for r in record]) - np.min([r[feature] for r in record]) for feature in feature_names])


def sampling_rate_consistency(record):
    record = normalize_timestamp(record)
    sampling = [record[i + 1]['timestamp'] - record[i]['timestamp'] for i in range(len(record) - 1)]
    sampling_trunc = [round(r, 3) for r in sampling]
    return consistency(sampling), np.median(sampling), mode(sampling_trunc)


def count_missing_segments(record, sample_mode):
    missing_segment_count = 0
    inserts = []
    missing_amount = 0
    for i, r in enumerate(record[:-1]):
        if record[i + 1]['timestamp'] - record[i]['timestamp'] > sample_mode * 20:
            missing_segment_count += 1
            missing_amount += record[i + 1]['timestamp'] - record[i]['timestamp']
            inserts.append(i)
    for count, i in enumerate(inserts):
        record = record[:i + 1 + count * 20] + [{'univariate_value': 0, 'inserted': True}] * 20 + record[i + 1 + count * 20:]

    return missing_amount, missing_segment_count, record