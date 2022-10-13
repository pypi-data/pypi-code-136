import numpy as np

def laplace_mechanism(value : float, sensitivity: float, epsilon:float, seed=0):
    if epsilon == 0 :
        return value
    np.random.seed(seed)
    scale = sensitivity/epsilon
    noise = np.random.laplace(0, size=1, scale=scale)
    return value + noise.item()
