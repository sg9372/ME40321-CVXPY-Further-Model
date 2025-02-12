import cvxpy as cp
import numpy as np

def total_weight_change_optimize(values, emissions, old_weights):
    n = len(values)
    
    # Variable to optimize
    weights = cp.Variable(n)

    # Weighting of how much we care about emissions relative to weights e.g. $1 per 1kg CO2e
    alpha = 1   # Emissions
    beta = 0.3    # Returns

    # Define objective function
    objective = cp.Minimize(alpha * cp.sum(cp.multiply(emissions, weights)) - 
                            beta * cp.sum(cp.multiply(values, weights)))

    # Calculate current emissions
    

    # Define constraints
    constraints = [
        cp.sum(weights) == 1,
        weights >= 0,
        cp.sum(cp.abs(weights - old_weights)) <= 0.05,  # Total change in weights
        cp.sum(cp.multiply(emissions, weights)) <= 50   # Emissions cap
    ]

    # Solve
    prob = cp.Problem(objective, constraints)
    prob.solve()

    # Output Weights
    return weights.value