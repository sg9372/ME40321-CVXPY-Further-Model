import unittest
import numpy as np
import cvxpy as cp
from src.total_weight_change_limit import total_weight_change_optimize

class test_total_weight_change_optimize(unittest.TestCase):

    # Expected not to adjust weights
    def test_UnchangedWeights(self):
        values = np.array([1,1,0])
        emissions = np.array([0,0,1])
        old_weights = np.array([0.5,0.5,0])
        weights = total_weight_change_optimize(values, emissions, old_weights)
        assert np.all(np.abs(weights - old_weights) <= 0.001)
    
    # Expected to change to [0.025, 0.5, 0.0475]
    def test_ChangedWeights(self):
        values = np.array([1,1,0])
        emissions = np.array([0,1,1])
        old_weights = np.array([0,0.5,0.5])
        weights = total_weight_change_optimize(values, emissions, old_weights)
        correct = np.array([0.025,0.5,0.475])
        assert np.all(np.abs(weights - correct) <= 0.001)