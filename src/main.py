import cvxpy as cp
import numpy as np

# Example variables
n = 10  # Number of assets
returns = np.random.rand(n)
emissions = np.random.rand(n)

# Original (fixed) weights before optimization
old_weights = np.random.rand(n)
old_weights /= old_weights.sum()  # Normalize to sum to 1

# Variable to optimize
weights = cp.Variable(n)

alpha = 1
beta = 0.5

objective = cp.Minimize(alpha * cp.sum(cp.multiply(emissions, weights)) - 
                        beta * cp.sum(cp.multiply(returns, weights)))

constraints = [
    cp.sum(weights) == 1,
    weights >= 0,
    cp.abs(weights - old_weights) <= 0.01,
    cp.sum(cp.multiply(emissions, weights)) <= 50  # Emissions cap
]

prob = cp.Problem(objective, constraints)
prob.solve()

# Output
print("Original weights:", old_weights)
print("Optimal weights:", weights.value)