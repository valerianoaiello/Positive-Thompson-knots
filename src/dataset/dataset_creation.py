import csv
import numpy as np
from sympy.combinatorics import Permutation

from src.math_library.monoid_elements_generator import MonoidElementsGenerator
import src.math_library.positive_bt_permutations as positive_bt_permutations


def create_dataset(monoid_elements: np.ndarray, csv_path: str):
    _, width = monoid_elements.shape
    with open(csv_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow([
            'leaves',
            *['x' + str(i) for i in range(width)],
            'bottom_permutation',
            'top_permutation',
            'permutation',
            'orbits'
        ])
        for i in range(len(monoid_elements)):
            monoid_element = np.array(monoid_elements[i][:])
            # monoid_element = np.insert(monoid_element, 0, 1, axis=0)
            number_of_leaves = positive_bt_permutations.number_of_leaves(
                monoid_element)
            bottom_permutation = Permutation(
                positive_bt_permutations.bottom_permutation(number_of_leaves))
            top_permutation = Permutation(
                positive_bt_permutations.top_permutation(number_of_leaves, monoid_element))
            whole_permutation = positive_bt_permutations.whole_permutation(
                number_of_leaves, monoid_element)
            writer.writerow(
                [number_of_leaves] +
                [monoid_element[i] for i in range(width)] +
                [bottom_permutation, top_permutation,
                    whole_permutation, len(whole_permutation)]
            )


if __name__ == '__main__':
    HEIGHT = 2
    WIDTH = 2
    
    csv_path = 'data_w' + str(WIDTH) + 'h' + str(HEIGHT) + '.csv'

    monoid_elements = MonoidElementsGenerator(
        HEIGHT, WIDTH).generate_monoid_elements()

    create_dataset(monoid_elements, csv_path)
