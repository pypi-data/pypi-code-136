from odvalue.utils import Desolver
import numpy as np
import matplotlib.pyplot as plt

# 例子来源于朱位秋的论文StochasticAveragingOf.aaasiNonintegrable-Hamiltonl Systems, 1997
# 绘制概率密度函数

# 函数的定义需遵守t, y(可多维), ..., **kwargs 形式

def deter_func(t, yn, alpha1, beta1, oumiga1, alpha2, beta2, oumiga2, a, b, **kwargs):
    Y = np.zeros(4) # 与方程维度一致

    Y[0] = yn[1]
    Y[1] = alpha1 * yn[1] - beta1 * yn[0] ** 2 * yn[1] - (oumiga1 ** 2) * yn[0] - a * yn[2] - b * ((yn[0] - yn[2]) ** 3)
    Y[2] = yn[3]
    Y[3] = (alpha1 - alpha2) * yn[3] - beta2 * (yn[2] ** 2) * yn[3] - (oumiga2 ** 2) * yn[2] - a * yn[0] - b * ((yn[2] - yn[0]) ** 3)
    return Y

def rand_func(t, yn, c1, c2, h, D1, D2, **kwargs):
    # 因为每次去算k的时候噪声都会重新生成，所以切忌把这个函数并入确定性方程中
    Y = np.zeros(4)  # 与方程维度一致

    bro = [np.random.standard_normal() * np.sqrt(2 * h * D1), np.random.standard_normal() * np.sqrt(2 * h * D2)] # 生成高斯白噪声

    Y[0] = 0
    Y[1] = c1*yn[0]*bro[0]
    Y[2] = 0
    Y[3] = c2*yn[2]*bro[1]
    return Y


y0 = [0, 1, 0, 1]

para_dict = {
    # 求解设置
    'tspan': 10000,
    'h': 0.01,
    'rand_open': True,
    'slvtype': 'RK4',


    # 参数设置
    'alpha1': 0.01,
    'alpha2': 0.01,
    'beta1': 0.01,
    'beta2': 0.02,
    'oumiga1': 1,
    'oumiga2': 2,
    'a': 0.01,
    'b': 1,
    'c1': 1,
    'c2': 1,
    'D1': 0.3, # 噪声强度
    'D2': 0.3,
}

desolver = Desolver(deter_func, rand_func, y0, **para_dict)
data_solve = desolver.solver()

H = data_solve[1, :] ** 2 / 2 + data_solve[3, :] ** 2 / 2 + \
    (data_solve[0, :] * para_dict['oumiga1']) ** 2 / 2 + (data_solve[2, :] * para_dict['oumiga2']) ** 2 / 2 + \
    data_solve[0, :] * para_dict['a'] * data_solve[2, :] + para_dict['b'] * (data_solve[0, :] - data_solve[2, :]) ** 4 / 4

drop_rio = 0.2

stable = H[int(len(H) * drop_rio):]

# np.histogram(stable, bins=10, range=None, weights=None, density=True)
plt.hist(stable, density=True)
plt.show()
