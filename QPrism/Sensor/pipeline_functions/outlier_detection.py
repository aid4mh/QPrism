from pyod.models.feature_bagging import FeatureBagging
import pandas as pd
from QPrism.Sensor.pipeline_functions.preprocessing import *

import warnings
warnings.filterwarnings("ignore")

def detect_outliers(record, feature_names):
    if len(feature_names) == 1:
        record[feature_names[0]+'extra42'] = record[feature_names[0]]
        feature_names.append(feature_names[0]+'extra42')
    record = features_to_float(record, feature_names)
    clf = FeatureBagging()
    clf.fit(record[feature_names].fillna(0))
    decision_scores = clf.decision_scores_
    return decision_scores


def outlier_counts(decision_scores):
    std = np.std(decision_scores)
    avg = np.mean(decision_scores)
    return [ i for i, d in enumerate(decision_scores) if d > avg+3*std ]

 
def count_outliers(record, feature_names):
    record = record.copy()
    record = features_to_float(record,feature_names)
    record = pd.DataFrame.from_dict(record)
    record = normalize_timestamp(record, ((list(record.keys()))[0]))
    record = features_to_float(record, feature_names)
    record = multi_var_to_uni(record, feature_names)
    decision_scores = detect_outliers(record, feature_names)

    record['decision_scores'] = decision_scores
    outlier_index = outlier_counts(decision_scores)
    return len(outlier_index)/len(record), outlier_index


def count_anomalous_segments(changepoints, outlier_locations, record_set):
    fail = 0
    succeed = 0
    if len(changepoints) > 0:
        change_ranges = [[0, changepoints[0]]] + [[changepoints[i], changepoints[i + 1]] for i in
                                                  range(len(changepoints[:-1]))] + [[changepoints[-1], len(record_set)]]
    else:
        change_ranges = []
        fail = 1
    for i, change in enumerate(change_ranges):
        if sum([r['univariate_value'] for r in record_set[i]]) != 0:
            for outlier in outlier_locations:
                if outlier > change[1]:
                    succeed += 1
                    break
                if outlier > change[0] and outlier < change[1]:
                    fail += 1
                    break
    return succeed/((succeed+fail) if succeed+fail> 0 else 1)