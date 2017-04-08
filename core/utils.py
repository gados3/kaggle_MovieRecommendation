import math


def min_max_normalization(min_val, max_val, val):
    return float(val - min_val) / (max_val - min_val)


def nominal_disimilarity(val_1, val_2):
    return int(val_1 != val_2)


def euclidian_distance(val_1, val_2):
    return minkowski_distance(val_1, val_2, 2)


def manhattan_distance(val_1, val_2):
    return abs(val_1 - val_2)


def minkowski_distance(val_1, val_2, power):
    return math.pow(val_1 - val_2, power)**(1. / power)


def global_dissimilarity(dissimilarities_array):
    numerator = 0
    for i in range(0, len(dissimilarities_array)):
        numerator += 1 * dissimilarities_array[i]
    return float(numerator) / len(dissimilarities_array)


def global_similarity(dissimilarities_array):
    return 1 - global_dissimilarity(dissimilarities_array)


def list_similarity(list_1, list_2):
    matches = set(list_1).intersection(list_2)
    if len(matches) > 0:
        return float(len(matches)) / max(len(list_1), len(list_2))
    else:
        return 0
