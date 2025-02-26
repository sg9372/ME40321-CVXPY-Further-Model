import cvxpy as cp
import numpy as np

def average_optimizer(values, emissions, old_weights):
    n = len(old_weights)
    
    # Variable to optimize
    weights = cp.Variable(n)

    # Weighting of how much we care about emissions relative to weights e.g. $1 per 1kg CO2e
    alpha = 1   # Emissions
    beta = 0  # Returns

    # Define objective function
    objective = cp.Minimize(alpha * cp.sum(cp.multiply(emissions, weights)) - 
                            beta * cp.sum(cp.multiply(values, weights)))

    # Calculate current emissions and value
    old_emissions = np.sum(emissions * old_weights)
    old_values = np.sum(values * old_weights)

    # Define constraints
    constraints = [
        cp.sum(cp.multiply(emissions, weights)) <= old_emissions,   # Emissions cap
        cp.sum(cp.multiply(values, weights)) >= old_values,         # Values limit
        cp.sum(weights) == 1,
        weights >= 0,
        #cp.sum(cp.abs(weights - old_weights)) <= 0.5,  # Total change in weights
        cp.abs(weights - old_weights) <= 0.001,    
    ]

    # Solve
    prob = cp.Problem(objective, constraints)
    prob.solve()

    # Output Weights
    return weights.value