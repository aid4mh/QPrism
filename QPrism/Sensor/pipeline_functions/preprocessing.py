import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def standard_scaler(col, feature_names):
    scaler = StandardScaler()
    try:
        return scaler.fit_transform(X=col.to_numpy().reshape(-1, 1))
    except:
        for key in list(feature_names):
            new_vals = scaler.fit_transform(X= np.asarray([c[key] for c in col]).reshape(-1, 1))
            for i, val in enumerate(new_vals):
                col[i][key] = val[0]
        return col


def normalize_timestamp(record, time_keyname):
    try:
        record[time_keyname] = record[time_keyname] - int(record[time_keyname].iloc[0])
        return record
    except:
        start = record[0][time_keyname]
        for i in range(len(record)):
            record[i][time_keyname] =  record[i][time_keyname]- start
        return record


def min_max_scaler(col):
    scaler = MinMaxScaler()
    return scaler.fit_transform(X=col.to_numpy().reshape(-1, 1))


def multi_var_to_uni(record, cols):
    record['univariate_value'] = np.sqrt(np.square(record[cols]).sum(axis=1))
    return record


def features_to_float(record, feature_names):
    try:
        for feature in feature_names:
            record[feature] = record[feature].astype(float)
        return record
    except:
        for i in range(len(record)):
            for feature in feature_names:
                record[i][feature] = float(record[i][feature])
        return record