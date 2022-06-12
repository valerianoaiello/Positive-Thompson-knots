import numpy as np
from sympy.combinatorics import Permutation
import csv

from entities.tree import generate_vectors, random_generate_vectors, number_leaves_ternary, bottom_permutation, top_permutation, whole_permutation
from constants import (
    VECTOR_NUMBER,
    RANDOM_HEIGHT_VECTOR,
    RANDOM_WIDTH_VECTOR,
    HEIGHT_VECTOR,
    WIDTH_VECTOR
)
a = WIDTH_VECTOR #number components in basis vectors
b = HEIGHT_VECTOR

c = RANDOM_WIDTH_VECTOR
d = RANDOM_HEIGHT_VECTOR
e = VECTOR_NUMBER

generate_vectors_parameters = [a, b]
random_generate_vectors_parameters = [e, d, c]

widths = [a, c]

function_parameters = [generate_vectors_parameters, random_generate_vectors_parameters]
names_list = ['data.csv', 'random_data.csv']
functions_list = [generate_vectors, random_generate_vectors]

for j in range(2):
    # A = generate_vectors(a,b) 
    A = functions_list[j](*function_parameters[j])
    #a=height
    #b=width

    with open(names_list[j], 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['leaves', *['x'+str(i) for i in range(widths[j])], 'bottom_permutation', 'top_permutation','permutation', 'orbits'])
        for i in range(len(A)):
            v = np.array(A[i][:])
            v = np.insert(v, 0, 1, axis=0)
            n = number_leaves_ternary(v)
            q = Permutation(bottom_permutation(n))
            p = Permutation(top_permutation(n, v))
            r = whole_permutation(n, v)
            writer.writerow([n] + [v[i] for i in range(a)] +[q, p, r, len(r)])


