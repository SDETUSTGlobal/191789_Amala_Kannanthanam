from scipy.special import exp10
#define exp10 function and pass value in its
exp = exp10([1,10])
print(exp)

#2
from scipy.special import comb
#find combinations of 5, 2 values using comb(N, k)
com = comb(5, 2, exact = False, repetition=True)
print(com)

#3
from scipy.special import perm
#find permutation of 5, 2 using perm (N, k) function
per = perm(5, 2, exact = True)
print(per)


