import numpy as np
from scipy.optimize import minimize


# define function f(x)
def f(x):
    return .4 * (1 - x[0]) ** 2


optimize.minimize(f, [2, -1], method="Nelder-Mead")
