# In this file, given the normal form of positive element g of F expressed as a vector v,
# we compute a vector w=(a,b) such that the number of connected components of L(g) is contained in
# the interval [a,b]
from turtle import shape
import numpy as np
from sklearn.metrics import v_measure_score
from sympy.combinatorics import Permutation
from tree import number_leaves_ternary




# This function works for elements of F_{3,+}, the number of leaves n is always an odd number
# the index i is always even
def components_interval(v: np.ndarray) -> np.ndarray:
    n = number_leaves_ternary(v)
    interval_components=np.array([0, 0])
    print('nonzero(v)',np.nonzero(v))
    print('length:',len(np.nonzero(v)[0]))
    nonzero_indices = np.nonzero(v)[0]
    index_last_nonzero_entry = len(nonzero_indices)-1
    while len(np.nonzero(v))>=1:
        if v[index_last_nonzero_entry]==1 and v[index_last_nonzero_entry-2]!=0:#case A
            interval_components = interval_components +np.array([1, 1])
            v[index_last_nonzero_entry]=0
            n=n-2
        elif v[index_last_nonzero_entry]==1 and v[index_last_nonzero_entry-2]==0 and v[index_last_nonzero_entry-4]>=2:#case B
            v[index_last_nonzero_entry]=0
            v[index_last_nonzero_entry-4]=v[index_last_nonzero_entry-4]-1
            n=n-4
        elif v[index_last_nonzero_entry]>=2:#case C
            interval_components = interval_components+np.array([-1, 1])
            v[index_last_nonzero_entry] = v[index_last_nonzero_entry] -1 
            n=n-2
        nonzero_indices = np.nonzero(v)[0]
        index_last_nonzero_entry = len(nonzero_indices)-1
    if n!=0:
        interval_components = interval_components + np.array([(n+1)/2, (n+1)/2]) 
    return interval_components
 

if __name__ == '__main__':
#    v = np.array([0,  0, 0,  0, 0,  0, 0,  0, 0])
    v = np.array([1, 0, 1, 0, 0])
    n=7
    print('v=',v,'n=',n)
    w = components_interval(v,n)
    print(w)

"""
    while np.count_nonzero(v)!=0:
        if v[i]==1 and v[i-2]!=0:#case A
            w=w+np.array([1, 1])
            v[i]=v[i]-1
            v[i-2]=v[i-2]-1
            n=n-2
        elif v[i]==1 and v[i-4]>=2:#case B
            w=w
            v[i]=v[i]-1
            v[i-4]=v[i-4]-2
            n=n-4
        elif v[i]>=2:
            w=w+np.array([-1, 1])
            v[i]=0
            n=n-2
        print('v=',v) 
        i=v[len(np.nonzero(v)[0])]
    if n!=0 and np.count_nonzero(v)==0:
        w=w+(n+1)/2



    i=v[len(np.nonzero(v)[0])]
    print('i=',i)
    print('v=',v)
    print('v[1]=',v[1])
    print('w=',w)
"""