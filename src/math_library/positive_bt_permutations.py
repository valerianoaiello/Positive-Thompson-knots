import numpy as np
from sympy.combinatorics import Permutation

"""
v = (v_1, v_2, ..., v_n)
0 <= v_i < m, v_i in N, for every i
"""


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
        trifurcation_points = int((number_of_leaves - 3)/2) # (number of vertices of degree 4) - 1 in a bottom tree of a positive element
        for i in range(trifurcation_points):
            temp_permutation = Permutation(temp_permutation(2*i + 1, 2*i + 4))
        permutation = Permutation(temp_permutation(number_of_leaves - 2, number_of_leaves))
    
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

        last_non_zero_exp_index = non_zero_exp_indices[len(non_zero_exp_indices) - 1]

        v_prime = monoid_element.copy()
        v_prime[last_non_zero_exp_index] = v_prime[last_non_zero_exp_index] - 1

        w = top_permutation(number_of_leaves - 2, v_prime)
        permutation = np.zeros(number_of_leaves + 1).astype(int)
        for i in range(number_of_leaves - 1):
            if i <= last_non_zero_exp_index and w[i] <= last_non_zero_exp_index:
                permutation[i] = w[i]
            elif i <= last_non_zero_exp_index and w[i] == last_non_zero_exp_index + 1:
                permutation[i] = w[i] + 1
            elif i <= last_non_zero_exp_index and w[i] >= last_non_zero_exp_index + 2:
                permutation[i] = w[i] + 2
            elif i >= last_non_zero_exp_index + 2 and w[i] >= last_non_zero_exp_index + 2:
                permutation[i + 2] = w[i] + 2
            elif i >= last_non_zero_exp_index + 2 and w[i] <= last_non_zero_exp_index:
                permutation[i + 2] = w[i]
            elif i >= last_non_zero_exp_index + 2 and w[i] == last_non_zero_exp_index + 1:
                permutation[i + 2] = last_non_zero_exp_index + 2
            elif i == last_non_zero_exp_index + 1 and w[i] >= last_non_zero_exp_index + 2:
                permutation[i + 1] = w[i] + 2
            elif i == last_non_zero_exp_index + 1 and w[i] <= last_non_zero_exp_index:
                permutation[i + 1] = w[i]
        permutation[last_non_zero_exp_index + 1] = last_non_zero_exp_index + 3
        permutation[last_non_zero_exp_index + 3] = last_non_zero_exp_index + 1
    return permutation


def whole_permutation(number_of_leaves: int, monoid_element: np.ndarray) -> np.ndarray:
    top_permutation_ = top_permutation(number_of_leaves, monoid_element)
    bottom_permutation_ = bottom_permutation(number_of_leaves)

    tot = []

    for i in range(number_of_leaves):
        l: list = []
        if i not in [item for sublist in tot for item in sublist]:
            while True:
                if top_permutation_[i] not in l:
                    l.append(top_permutation_[i])
                    i = top_permutation_[i]
                    if bottom_permutation_[i] not in l:
                        l.append(bottom_permutation_[i])
                        i = bottom_permutation_[i]
                    else:
                        break
                else:
                    break
            tot.append(l)
    return tot

# this function find the number of leaves in the reduced ternary tree representing an element in F_{3,+}


def number_of_leaves(monoid_element: np.ndarray) -> int:
    z = np.nonzero(monoid_element)[0]
    k = len(z)
    m = 1000
    w = np.array(list(range(m)))
    u = w.copy()
    for i in range(k - 1, -1, -1):
        for j in range(monoid_element[z[i]]):
            w = np.delete(w, z[i] + 1)
            w = np.delete(w, z[i] + 1)
    n = 0
    for i in range(len(w) - 1):
        if w[i + 1] - w[i] >= 2:
            n = w[i + 1]
    if n % 2 == 1:
        n = n + 2
    else:
        n = n + 1
    return n


if __name__ == '__main__':
    print(np.array(Permutation(bottom_permutation(5)).array_form))
    print(top_permutation(5, np.array([1, 0, 0])))
