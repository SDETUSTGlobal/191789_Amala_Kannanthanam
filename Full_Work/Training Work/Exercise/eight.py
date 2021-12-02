import matplotlib.pyplot as plt
from scipy import optimize
import numpy as np

def function(a):
       return   a*2 + 20 * np.sin(a)
plt.plot(a, function(a))
plt.show()
#use BFGS algorithm for optimization
optimize.fmin_bfgs(function, 0)
