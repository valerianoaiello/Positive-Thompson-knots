import numpy as np
from sympy.combinatorics import Permutation
import time
import csv
import sklearn

from tree import generate_vectors, number_leaves_binary, number_leaves_ternary, bottom_permutation, top_permutation
from tree_2 import whole_permutation_2


a=4#number components in basis vectors
b=3#exponents
A=generate_vectors(a,b) 
#a=height
#b=width


# n=number_leaves_ternary(np.array([1][:]))
# q=Permutation(bottom_permutation(n))
# p=Permutation(top_permutation(n, np.array(A[1][:])))
# r=p*q
# print(n,A[2][:],q,p)
with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['leaves', 'vector', 'bottom_permutation', 'top_permutation','permutation', 'orbits'])

    for i in range(1,b**a):
        v=np.array(A[i][:])
        n=number_leaves_ternary(v)
        q=Permutation(bottom_permutation(n))
        p=Permutation(top_permutation(n, v))
        r=whole_permutation_2(n,A[i][:])
#        print(n,v,q,p)
        writer.writerow([n, A[i][:], q, p, r, len(r)])
# ###       print(A[i][:].shape)
