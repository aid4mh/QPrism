import numpy as np
import scipy.stats as stats

def classify_activities(record_set, record_len):
    n = len(record_set)
    Seg_Class = []
    for j in range(n):
        vals = [r['univariate_value'] for r in record_set[j] if 'inserted' not in r]
        if len(vals)>1:
            var = stats.variation(vals)
            if var < 0.01:
                Seg_Class.append(0)
            else:
                Seg_Class.append(1)
    for j in range(2, len(Seg_Class)):
        if j > 1:
            if (Seg_Class[j-1] and not (Seg_Class[j - 2]) and Seg_Class[j]) and (len(record_set[ j-1]) < record_len*.01):  # preceding seg is non-wear, following seg is non-wear, this seg is normal AND shorter than 1 sec --> 5 points
                Seg_Class[j-1] = 2

    return Seg_Class

def spurious_segment_density(Seg_Class):
    return len([s for s in Seg_Class if s == 2]) / len(Seg_Class)

def activity_density(Seg_Class):
    return len([s for s in Seg_Class if s == 1]) / len(Seg_Class)
def non_activity_segment_density(Seg_Class):
    return len([s for s in Seg_Class if s == 0]) / len(Seg_Class)