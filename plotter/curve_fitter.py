import numpy as np
from scipy.optimize import curve_fit


def curve_fitting(func, x_data, y_data):
    params, params_covariance = curve_fit(func, x_data, y_data)
    return np.array(params)

def func_example(x, a, b, c):
    return a * np.exp(-b * x) + c

x = np.linspace(0, 4, 50)
y = func_example(x, 2.5, 1.3, 0.5)

optimized_params = curve_fitting(func_example, x, y)

print("Les paramètres optimisés sont : ", optimized_params)