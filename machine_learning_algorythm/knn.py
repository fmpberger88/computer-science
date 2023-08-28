import pandas as pd
import numpy as np
from distance_formula.euclidean_distance import euclidean_distance



# classifier
def classify(unknown, dataset, k):
    distances = []
    # Looping through all points in the dataset
    for element in dataset:
        distance_to_point = euclidean_distance(element, unknown)
        # Adding the distance and point associated with that distance
        distances.append([distance_to_point, element])
    distances.sort()
    # Taking only the k closest points
    neighbors = distances[0:k]


