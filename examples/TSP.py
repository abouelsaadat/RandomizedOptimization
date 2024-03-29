""" """

# Author: Mohamed Abouelsaadat
# License: MIT

import math
import numpy as np
import matplotlib.pyplot as plt
import randoptma.algorithms.mimic.algo as mimic_algo
import randoptma.algorithms.genetic.algo as genetic_algo
import randoptma.algorithms.simanneal.algo as simanneal_algo
import randoptma.algorithms.randhillclimb.algo as randhillclimb_algo


def euclidean_distance(pointA, pointB):
    return math.sqrt((pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2)


def TSP(input_x, positions):
    """Cities are visited based on their values ascending order,
    where cities with equal values are visited in their index order"""
    total = 0
    order = np.argsort(input_x, kind="mergesort")
    for itr in range(len(order)):
        total += euclidean_distance(
            positions[order[itr], :], positions[order[itr - 1], :]
        )
    return -total


ENTRY_LENGTH = 10
positions = np.random.default_rng().uniform(0, 100, (ENTRY_LENGTH, 2))
plt.scatter(positions[:, 0], positions[:, 1])


def problem_eval_function(input):
    return TSP(input, positions)


def problem_feat_dict():
    return {feat: list(range(ENTRY_LENGTH)) for feat in range(ENTRY_LENGTH)}


best_sample, best_score, *_ = mimic_algo.optimize(
    problem_feat_dict(),
    problem_eval_function,
)
print("smallest distance: ", -best_score)
print(
    "best travelling order: ",
    ";".join(str(int(bit)) for bit in np.argsort(best_sample)),
)

ordered_positions = positions[np.argsort(best_sample)]
plt.plot(ordered_positions[:, 0], ordered_positions[:, 1])
plt.show()
