import cvxpy as cp
import numpy as np

def average_optimizer(values, emissions, old_weights, sector_indices, end_of_last_sector_portfolio_value=None):
    print("Values", values)
    #print("Emissions", emissions)
    #print("Old Weights", old_weights)
    #print("Sector Indices", sector_indices)

    
    n = len(old_weights)

    # Variable to optimize
    weights = cp.Variable(n)

    # Define objective function to minimize change between weights and old_weights
    objective = cp.Minimize(cp.norm(weights - old_weights, 1))

    # Calculate current emissions and value
    old_emissions = np.sum(emissions * old_weights)
    old_values = np.sum(values * old_weights)

    sector_limit = 0.025  # maximum weight per sector

    if end_of_last_sector_portfolio_value is not None:
        portfolio_value = end_of_last_sector_portfolio_value
    else:
        portfolio_value = np.sum(values * old_weights)

    print("Portfolio value", portfolio_value)

    predicted_portfolio_value = cp.sum(cp.multiply(values, weights))

    #objective = cp.Maximize(predicted_portfolio_value-portfolio_value)


    # Define constraints
    constraints = [
        cp.sum(cp.multiply(emissions, weights)) <= old_emissions*0.8,   # Emissions cap
        cp.sum(weights) == 1,
        weights >= 0,
        cp.sum(cp.multiply(values, weights)) == portfolio_value,  # Means we can't magic in more money
        cp.sum(cp.abs(weights - old_weights)) <= 0.2,  # Total change in weights
    ]

    for indices in sector_indices:
        if indices:
            constraints.append(cp.sum(cp.abs(weights[indices] - old_weights[indices])) <= sector_limit)    

    # Solve
    prob = cp.Problem(objective, constraints)
    
    prob.solve(verbose=False)

    # Output Weights
    return weights.value