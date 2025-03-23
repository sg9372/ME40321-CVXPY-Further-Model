import cvxpy as cp
import numpy as np

def average_optimizer(values, emissions, old_weights, current_values,sector_indices):
    n = len(old_weights)

    # Variable to optimize
    weights = cp.Variable(n)

    # Define objective function to minimize change between weights and old_weights
    objective = cp.Minimize(cp.norm(weights - old_weights, 1))

    # Calculate current emissions and value
    old_emissions = np.sum(emissions * old_weights)
    old_values = np.sum(values * old_weights)

    sector_limit = 0.025  # maximum weight per sector

    # Define constraints
    constraints = [
        cp.sum(cp.multiply(emissions, weights)) <= old_emissions*0.8,   # Emissions cap
        cp.sum(cp.multiply(values, weights)) >= old_values*0.98,         # Values limit
        cp.sum(weights) == 1,
        weights >= 0,
        cp.sum(cp.multiply(current_values, weights)) == cp.sum(cp.multiply(current_values, old_weights)), # Means we can't magic in more money
        cp.sum(cp.abs(weights - old_weights)) <= 0.15,  # Total change in weights
        #cp.sum(cp.abs(weights - old_weights)) <= 0.5,  # Total change in weights
        #cp.abs(weights - old_weights) <= 0.002, 
    ]

    for indices in sector_indices:
        if indices:
            constraints.append(cp.sum(cp.abs(weights[indices] - old_weights[indices])) <= sector_limit)    

    # Solve
    prob = cp.Problem(objective, constraints)
    
    prob.solve(verbose=False)

    # Output Weights
    return weights.value