#4
from scipy import linalg
import numpy as np
#define square matrix
two_d_array = np.array([ [4,5], [3,2] ])
#pass values to det() function
linalg.det( two_d_array )

#5
from scipy import linalg
import numpy as np
# define square matrix
two_d_array = np.array([ [4,5], [3,2] ])
#pass value to function inv()
linalg.inv( two_d_array )