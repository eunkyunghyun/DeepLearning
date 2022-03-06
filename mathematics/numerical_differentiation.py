# A brief example in the field of numerical differentiation exposed as:

import numpy as np


def numerical_derivative(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)


def func(x):
    return 3 * x * np.exp(x)


print(numerical_derivative(func, 2))
