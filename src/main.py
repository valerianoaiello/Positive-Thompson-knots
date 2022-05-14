import numpy as np
from sympy.combinatorics import Permutation
import time
import csv
import sklearn

from tree import generate_vectors, number_leaves_binary, number_leaves_ternary, bottom_permutation, top_permutation, whole_permutation
from constants import WIDTH_VECTOR

a = WIDTH_VECTOR #number components in basis vectors
b = 3#exponents
A = generate_vectors(a,b) 
#a=height
#b=width

with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['leaves', *['x'+str(i) for i in range(a)], 'bottom_permutation', 'top_permutation','permutation', 'orbits'])
    for i in range(1,b**a):
        v=np.array(A[i][:])
        v = np.insert(v, 0, 1, axis=0)
        n=number_leaves_ternary(v)
        q=Permutation(bottom_permutation(n))
        p=Permutation(top_permutation(n, v))
        r=whole_permutation(n,v)
        writer.writerow([n]+ [v[i] for i in range(a)] +[q, p, r, len(r)])


