import cvxpy as cp
import numpy as np

def total_weight_change_optimize(values, emissions, old_weights):
    n = len(values)
    
    # Variable to optimize
    weights = cp.Variable(n)

    # Weighting of how much we care about emissions relative to weights e.g. $1 per 1kg CO2e
    alpha = 1
    beta = 1

    # Define objective function
    objective = cp.Minimize(alpha * cp.sum(cp.multiply(emissions, weights)) - 
                            beta * cp.sum(cp.multiply(values, weights)))

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
    return weights
    '''
    print("Original weights:", np.round(old_weights*100,2))
    print("Optimal weights:", np.round(weights.value*100,2))

    # Output Emissions
    old_emissions = np.sum(emissions * old_weights)
    total_emissions = np.sum(emissions * weights.value)
    print("Old emissions:", np.round(old_emissions,2))
    print("New emissions:", np.round(total_emissions,2))

    # Output weights
    old_weights = np.sum(weights * old_weights)
    total_weights = np.sum(weights * weights.value)
    print("Old weights:", np.round(old_weights,2))
    print("New weights:", np.round(total_weights,2))
    '''