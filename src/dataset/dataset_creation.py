import csv
import numpy as np
from sympy.combinatorics import Permutation

from src.math_library.monoid_elements_generator import MonoidElementsGenerator
import src.math_library.positive_bt_permutations as positive_bt_permutations

HEIGHT = 2
WIDTH = 3

csv_name = 'data.csv'

monoid_elements = MonoidElementsGenerator(
    HEIGHT, WIDTH).generate_monoid_elements()

with open(csv_name, 'w') as f:
    writer = csv.writer(f)
    writer.writerow([
        'leaves',
        *['x' + str(i) for i in range(WIDTH)],
        'bottom_permutation',
        'top_permutation',
        'permutation',
        'orbits'
    ])
    for i in range(len(monoid_elements)):
        v = np.array(monoid_elements[i][:])
        v = np.insert(v, 0, 1, axis=0)
        n = positive_bt_permutations.number_of_leaves(v)
        q = Permutation(positive_bt_permutations.bottom_permutation(n))
        p = Permutation(positive_bt_permutations.top_permutation(n, v))
        r = positive_bt_permutations.whole_permutation(n, v)
        writer.writerow([] + [v[i] for i in range(WIDTH)] + [q, p, r, len(r)])
