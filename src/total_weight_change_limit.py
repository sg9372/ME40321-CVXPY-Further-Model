import cvxpy as cp
import numpy as np

# Define variables
n = 10  # Number of assets
returns = np.random.rand(n)*50
emissions = np.random.rand(n)*50

# Original (fixed) weights before optimization
old_weights = np.random.rand(n)
old_weights /= old_weights.sum()  # Normalize to sum to 1

# Variable to optimize
weights = cp.Variable(n)

# Weighting of how much we care about emissions relative to returns e.g. $1 per 1kg CO2e
alpha = 1
beta = 1

# Define objective function
objective = cp.Minimize(alpha * cp.sum(cp.multiply(emissions, weights)) - 
                        beta * cp.sum(cp.multiply(returns, weights)))

# Define constraints
constraints = [
    cp.sum(weights) == 1,
    weights >= 0,
    cp.sum(cp.abs(weights - old_weights)) <= 0.05,  # Total change in weights
    cp.abs(weights - old_weights) <= 0.01,          # Max change in any individual weight
    cp.sum(cp.multiply(emissions, weights)) <= 50   # Emissions cap
]

# Solve
prob = cp.Problem(objective, constraints)
prob.solve()

# Output Weights
print("Original weights:", np.round(old_weights*100,2))
print("Optimal weights:", np.round(weights.value*100,2))

# Output Emissions
old_emissions = np.sum(emissions * old_weights)
total_emissions = np.sum(emissions * weights.value)
print("Old emissions:", np.round(old_emissions,2))
print("New emissions:", np.round(total_emissions,2))

# Output Returns
old_returns = np.sum(returns * old_weights)
total_returns = np.sum(returns * weights.value)
print("Old returns:", np.round(old_returns,2))
print("New returns:", np.round(total_returns,2))