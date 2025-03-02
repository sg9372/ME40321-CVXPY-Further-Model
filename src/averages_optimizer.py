import cvxpy as cp
import numpy as np

def average_optimizer(values, emissions, old_weights):
    n = len(old_weights)

    # Variable to optimize
    weights = cp.Variable(n)

    # Define objective function to minimize change between weights and old_weights
    objective = cp.Minimize(cp.norm(weights - old_weights, 1))

    # Calculate current emissions and value
    old_emissions = np.sum(emissions * old_weights)
    old_values = np.sum(values * old_weights)

    # Define constraints
    constraints = [
        cp.sum(cp.multiply(emissions, weights)) <= old_emissions*0.95,   # Emissions cap
        cp.sum(cp.multiply(values, weights)) >= old_values*0.98,         # Values limit
        cp.sum(weights) == 1,
        weights >= 0,
        #cp.sum(cp.abs(weights - old_weights)) <= 0.5,  # Total change in weights
        #cp.abs(weights - old_weights) <= 0.002,    
    ]

    # Solve
    prob = cp.Problem(objective, constraints)
    
    prob.solve(verbose=False)

    # Output Weights
    return weights.value