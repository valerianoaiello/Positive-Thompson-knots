import numpy as np
from sympy.combinatorics import Permutation
import csv

from src.math_library.math_utils import MathUtils
from src.global_constants.constants import (
    VECTOR_NUMBER,
    RANDOM_HEIGHT_VECTOR,
    RANDOM_WIDTH_VECTOR,
    HEIGHT_VECTOR,
    WIDTH_VECTOR
)

math_utils = MathUtils()
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
functions_list = [math_utils.generate_vectors, math_utils.random_generate_vectors]

for j in range(2):
    A = functions_list[j](*function_parameters[j])

    with open(names_list[j], 'w') as f:
        writer = csv.writer(f)
        writer.writerow([
            'leaves', 
            *['x'+str(i) for i in range(widths[j])], 
            'bottom_permutation', 
            'top_permutation',
            'permutation', 
            'orbits'
            ])
        for i in range(len(A)):
            v = np.array(A[i][:])
            v = np.insert(v, 0, 1, axis=0)
            n = math_utils.number_leaves_ternary(v)
            q = Permutation(math_utils.bottom_permutation(n))
            p = Permutation(math_utils.top_permutation(n, v))
            r = math_utils.whole_permutation(n, v)
            writer.writerow([n] + [v[i] for i in range(a)] +[q, p, r, len(r)])


