import numpy as np
from sympy.combinatorics import Permutation
import time
import csv
import sklearn

from tree import generate_vectors, number_leaves_binary, number_leaves_ternary, bottom_permutation, top_permutation


a=4#number components in basis vectors
b=3#exponents
A=generate_vectors(a,b) 
#a=height
#b=width

# with open('data.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['leaves', 'vector', 'bottom_permutation', 'top_permutation','permutation', 'orbits'])

#     for i in range(1,b**a):
#         n=number_leaves_ternary(np.array([i][:]))
#         q=Permutation(bottom_permutation(n))
#         p=Permutation(top_permutation(n, np.array(A[i][:])))
#         r=p*q
#         writer.writerow([n, A[i][:], q, p, r, r.cycles])
#        print(A[i][:].shape)
