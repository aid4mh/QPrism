import numpy as np
#import ruptures as rpt
#from sktime.annotation.clasp import ClaSPSegmentation

def updateLaplacePrediction(alphas, betas, x):
    alphas[:] += x
    betas[:] += (1 - x)
    alphas = np.append(alphas, 1)  # Creating new Forecaster
    betas = np.append(betas, 1)  # Creating new Forecaster
    return alphas, betas


def updateForecasterDistribution(ForecasterDistribution, alphas, betas, reward, gamma):
    if reward == 1:
        likelihood = np.divide(alphas, alphas + betas)
    else:
        likelihood = np.divide(betas, alphas + betas)
    ForecasterDistribution0 = gamma * np.dot(likelihood,
                                             np.transpose(ForecasterDistribution))  # Creating new Forecaster
    ForecasterDistribution = (1 - gamma) * likelihood * ForecasterDistribution  # update the previous forecasters
    ForecasterDistribution = np.append(ForecasterDistribution,
                                       ForecasterDistribution0)  # Including the new forecaseter into the previons ones
    ForecasterDistribution = ForecasterDistribution / np.sum(
        ForecasterDistribution)  # Normalization for numerical purposes
    return ForecasterDistribution


def BOCD(environment):
    # --------------- Initialization ---------------------
    Horizon = environment.size
    gamma = 1 / Horizon  # Switching Rate
    alphas = np.array([1])
    betas = np.array([1])
    ForecasterDistribution = np.array([1])
    ChangePointEstimation = np.array([])
    # -----------------------------------------------------
    # Interation with the environment ...
    for t in range(Horizon):
        EstimatedBestExpert = np.argmax(ForecasterDistribution)  # Change-point estimation
        ChangePointEstimation = np.append(ChangePointEstimation, EstimatedBestExpert + 1)
        reward = int((np.random.uniform() < environment[t]) == True)  # Get the observation from the environment
        ForecasterDistribution = updateForecasterDistribution(ForecasterDistribution, alphas, betas, reward, gamma)
        (alphas, betas) = updateLaplacePrediction(alphas, betas, reward)  # Update the laplace predictor
    return ChangePointEstimation


def pelt_changepoint(record, feature_names):
    changes = []
    for i, feature in enumerate(feature_names):
        found_pelt = rpt.Pelt(model="rbf").fit(record[feature].to_numpy())
        result = found_pelt.predict(pen=10)
        changes.append(result)
    return changes


def clasp_changepoint(record, feature_names, period_size):
    changes = []

    clasp = ClaSPSegmentation(period_length=period_size, n_cps=10, fmt="sparse")
    for i, feature in enumerate(feature_names):
        found_cps = clasp.fit_predict(record[feature])
        changes.append(found_cps)
    return changes



def bocd_changepoint(record, feature_names):
    changes = []

    for i,feature in enumerate(feature_names):
        ary = np.asarray([float(r[feature]) for r in record])
        if i == 0:
            changes = [list(dict.fromkeys(BOCD(ary)))]
        else:
            changes+=[list(dict.fromkeys(BOCD(ary)))]

    return changes[0] if len(feature_names) == 1 else changes

def single_feature_split(record, changes):
    return [record[:int(changes[0])]] + [record[int(r):int(r+1)] for i, r in enumerate(changes[:-1])] + [record[int(changes[-1]):]]

def multi_feature_split(record, changes, policy='all'):
    last = 0
    record_set = []
    while True:
        if policy == 'all':
            if min([len(c) for c in changes]) == 0:
                return record_set
            else:
                split = np.argmax([changes[i][0] for i in range(len(changes))])
                adjust = int(changes[split][0])
                record_set.append(record[last:adjust])
                last = adjust
                for i in range(len(changes)):
                    changes[i] = [x for x in changes[i] if x > adjust]
        if policy == 'any':
            if max([len(c) for c in changes]) == 0:
                return record_set
            else:
                split = np.argmin([changes[i][0] if len(changes[i]) > 0 else np.inf for i in range(len(changes))])
                adjust = int(changes[split][0])
                record_set.append(record[last:adjust])
                last = adjust
                changes[split] = changes[split][1:]

    
def perform_changepoint(record):
    changepoints = bocd_changepoint(record=record, feature_names=['univariate_value'])[1:]
    if len(changepoints) == 0:
        record_set = [record]
    else:
        record_set = single_feature_split(record, changes=changepoints)
    return record_set, changepoints