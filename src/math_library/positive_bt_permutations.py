import numpy as np
from sympy.combinatorics import Permutation


def bottom_permutation(number_of_leaves: int) -> np.ndarray:
    """
    This function computes the permutation associated with the bottom tree of a positive Thompson element
    n must be an odd number and the permutation acts on {0,1,...,n}
    """
    if number_of_leaves % 2 == 0:
        print('The number is even')
        exit(0)
    if number_of_leaves == 1:
        permutation = Permutation(0, 1)
    elif number_of_leaves == 3:
        permutation = Permutation(0, 2)(1, 3)
    else:
        temp_permutation = Permutation(0, 2)
        # (number of vertices of degree 4) - 1 in a bottom tree of a positive element
        trifurcation_points = int((number_of_leaves - 3)/2)
        for i in range(trifurcation_points):
            temp_permutation = Permutation(temp_permutation(2*i + 1, 2*i + 4))
        permutation = Permutation(temp_permutation(
            number_of_leaves - 2, number_of_leaves))

    return np.array(permutation.array_form)


def top_permutation(number_of_leaves: int, monoid_element: np.ndarray) -> np.ndarray:
    """
    This function computes the permutation associated with the top tree of a positive Thompson element.
    Arg:
    - n is odd number and the permutation acts on {0,1,...,n}
    """
    if number_of_leaves % 2 == 0:
        print('The number is even')
        exit(0)
    if number_of_leaves == 1:
        permutation = np.array([1, 0])
    elif number_of_leaves == 3:
        permutation = np.array([2, 3, 0, 1])
    elif number_of_leaves >= 5 and not np.any(monoid_element):
        permutation = bottom_permutation(number_of_leaves)
    else:
        non_zero_exp_indices = np.nonzero(monoid_element)[0]

        last_non_zero_exp_index = non_zero_exp_indices[len(
            non_zero_exp_indices) - 1]

        temp_monoid_element = monoid_element.copy()
        temp_monoid_element[last_non_zero_exp_index] = temp_monoid_element[last_non_zero_exp_index] - 1

        temp_permutation = top_permutation(
            number_of_leaves - 2, temp_monoid_element)
        permutation = np.zeros(number_of_leaves + 1).astype(int)
        for i in range(number_of_leaves - 1):
            if i <= last_non_zero_exp_index and temp_permutation[i] <= last_non_zero_exp_index:
                permutation[i] = temp_permutation[i]
            elif i <= last_non_zero_exp_index and temp_permutation[i] == last_non_zero_exp_index + 1:
                permutation[i] = temp_permutation[i] + 1
            elif i <= last_non_zero_exp_index and temp_permutation[i] >= last_non_zero_exp_index + 2:
                permutation[i] = temp_permutation[i] + 2
            elif i >= last_non_zero_exp_index + 2 and temp_permutation[i] >= last_non_zero_exp_index + 2:
                permutation[i + 2] = temp_permutation[i] + 2
            elif i >= last_non_zero_exp_index + 2 and temp_permutation[i] <= last_non_zero_exp_index:
                permutation[i + 2] = temp_permutation[i]
            elif i >= last_non_zero_exp_index + 2 and temp_permutation[i] == last_non_zero_exp_index + 1:
                permutation[i + 2] = last_non_zero_exp_index + 2
            elif i == last_non_zero_exp_index + 1 and temp_permutation[i] >= last_non_zero_exp_index + 2:
                permutation[i + 1] = temp_permutation[i] + 2
            elif i == last_non_zero_exp_index + 1 and temp_permutation[i] <= last_non_zero_exp_index:
                permutation[i + 1] = temp_permutation[i]
        permutation[last_non_zero_exp_index + 1] = last_non_zero_exp_index + 3
        permutation[last_non_zero_exp_index + 3] = last_non_zero_exp_index + 1
    return permutation


def whole_permutation(number_of_leaves: int, monoid_element: np.ndarray) -> np.ndarray:
    top_permutation_ = top_permutation(number_of_leaves, monoid_element)
    bottom_permutation_ = bottom_permutation(number_of_leaves)

    whole_permutation_ = []

    for i in range(number_of_leaves):
        whole_permutation_cycle: list = []
        if i not in [integer_ for cycle in whole_permutation_ for integer_ in cycle]:
            while True:
                if top_permutation_[i] not in whole_permutation_cycle:
                    whole_permutation_cycle.append(top_permutation_[i])
                    i = top_permutation_[i]
                    if bottom_permutation_[i] not in whole_permutation_cycle:
                        whole_permutation_cycle.append(bottom_permutation_[i])
                        i = bottom_permutation_[i]
                    else:
                        break
                else:
                    break
            whole_permutation_.append(whole_permutation_cycle)
    return whole_permutation_


def number_of_leaves(monoid_element: np.ndarray, max_dimension=1000) -> int:
    """
    This function find the number of leaves in the reduced ternary tree representing an element in F_{3,+}
    """
    non_zero_exp_indices = np.nonzero(monoid_element)[0]
    number_non_zero_exp_indices = len(non_zero_exp_indices)

    integer_interval = np.array(list(range(max_dimension)))

    for i in range(number_non_zero_exp_indices - 1, -1, -1):

        j = 0
        while j < monoid_element[non_zero_exp_indices[i]]:
            integer_interval = np.delete(
                integer_interval, non_zero_exp_indices[i] + 1)
            integer_interval = np.delete(
                integer_interval, non_zero_exp_indices[i] + 1)
            j = j + 1

    number_of_leaves_ = 0

    for i in range(len(integer_interval) - 1):
        if integer_interval[i + 1] - integer_interval[i] >= 2:
            number_of_leaves_ = integer_interval[i + 1]
    if number_of_leaves_ % 2 == 1:
        number_of_leaves_ = number_of_leaves_ + 2
    else:
        number_of_leaves_ = number_of_leaves_ + 1
    return number_of_leaves_


if __name__ == '__main__':
    # print(np.array(Permutation(bottom_permutation(5)).array_form))
    # print(top_permutation(5, np.array([1, 0, 0])))
    print(number_of_leaves([1, 0, 6]))
