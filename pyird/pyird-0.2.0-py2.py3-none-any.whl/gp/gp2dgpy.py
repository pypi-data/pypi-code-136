import GPy
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(seed=1)


kernel = GPy.kern.Matern32(2, ARD=True)
N = 100
X = np.random.uniform(-3.,3.,(N, 2))
Z = np.sin(X[:,0:1]) * np.sin(X[:,1:2]) + np.random.randn(N,1)*0.05

model = GPy.models.GPRegression(X, Z, kernel)
model.optimize(messages=True, max_iters=1e5)

## prediction
Nx=50
Ny=75
xgrid=np.linspace(-3, 3, Nx)
ygrid=np.linspace(-3, 3, Ny)

X1, X2 = np.meshgrid(xgrid,ygrid)
input_grid = np.array([X1.flatten(), X2.flatten()]).T
z_pred = model.predict_quantiles(input_grid, quantiles=(2.5, 50, 97.5))[1]
