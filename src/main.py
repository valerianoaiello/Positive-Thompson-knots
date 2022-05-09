import numpy as np
from sympy.combinatorics import Permutation
import time
import csv
import sklearn

from tree import generate_vectors, number_leaves_binary, number_leaves_ternary, bottom_permutation, top_permutation, whole_permutation


a=6#number components in basis vectors
b=3#exponents
A=generate_vectors(a,b) 
#a=height
#b=width

v=np.array([2, 2, 2, 1, 0, 0, 0, 0])
n=number_leaves_ternary(v)
with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['leaves', 'vector', 'bottom_permutation', 'top_permutation','permutation', 'orbits'])
    for i in range(1,b**a):
                v=np.array(A[i][:])
                for i in range(b):
                        for j in range(b):
                                if i!=j and i+j!=0:
                                        np.insert(v,i,j)
        #        print('v',v)
                n=number_leaves_ternary(v)
                q=Permutation(bottom_permutation(n))
                p=Permutation(top_permutation(n, v))
                r=whole_permutation(n,v)
                
        #        print(n,v,q,p)
                writer.writerow([n, v, q, p, r, len(r)])
# ###       print(A[i][:].shape)



        

    
