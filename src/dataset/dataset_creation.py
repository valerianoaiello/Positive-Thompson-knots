import numpy as np
from sympy.combinatorics import Permutation
import csv

from src.math_library.monoid_elements_generator import MonoidElementsGenerator
import src.math_library.positive_bt_permutations as positive_bt_permutations
from src.global_constants.constants import (
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

generate_vectors_parameters = []
random_generate_vectors_parameters = [e]

widths = [a, c]

function_parameters = [generate_vectors_parameters, random_generate_vectors_parameters]
names_list = ['data.csv', 'random_data.csv']
functions_list = [MonoidElementsGenerator(b, a).generate_monoid_elements, MonoidElementsGenerator(d, c).random_generate_monoid_elements]

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
            n = positive_bt_permutations.number_of_leaves(v)
            q = Permutation(positive_bt_permutations.bottom_permutation(n))
            p = Permutation(positive_bt_permutations.top_permutation(n, v))
            r = positive_bt_permutations.whole_permutation(n, v)
            writer.writerow([n] + [v[i] for i in range(a)] +[q, p, r, len(r)])


