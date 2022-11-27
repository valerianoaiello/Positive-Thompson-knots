import numpy as np
from sympy.combinatorics import Permutation
"""
Given an element g in F_{3,+} we associate a permutation to it.
The element is first described in its unique normal form as x_0^{a_0}\cdots x_n^{a_n} for some n (a natural number), 
a_0, ..., a_{n-1} (non-negative integers), a_n (positive integer).
The we consider the minimal ternary tree diagram representing it (this is given by a pair of ternary trees (T_+,T_-) with the same number of leaves).
The function "number_of_leaves" returns the number n of leaves of the trees in this minimal ternary tree diagram. 
The permutationo P(g) is going to act on {0, 1, 2, ..., n}.
First we construct two permutations on {0, 1, 2, ..., n}: the bottom permutation associated with T_- and the top permutation associated with T_+.
The former is produced by the function "bottom_permutation". Since the bottom tree of a positive element has always the same shape, the function takes only
one argument: the number of leaves.
The latter permutation is produced by the function "top_permutation" which takes two arguments: the number of leaves and the normal form of the 
element which is described by a vector v=(a_0,a_1, ..., a_n). 
By using these two permutations, we finally construct the Thompson permutation with the function "whole_permutation". This function takes two arguments: 
the number of leaves and the normal form of the element which is described by a vector v=(a_0,a_1, ..., a_n). 
"""

def bottom_permutation(number_of_leaves: int) -> np.ndarray:
    """
    This function computes the permutation associated with the bottom (ternary) tree of a positive Thompson element
    n must be an odd number and the permutation acts on {0,1,...,n}.
    We only need an argument in this function because a positive element has always the same shape.
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
    This function computes the permutation associated with the (ternary) top tree of a positive Thompson element.
    n is odd number and the permutation acts on {0,1,...,n}.
    The monoid element is represented as vector v=(a_0,a_1, ..., a_n).
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
    """
    This function computes the Thompson permutation associated with the ternary tree diagram of a positive Thompson element.
    n is odd number and the permutation acts on {0,1,...,n}.
    The monoid element g is represented as vector v=(a_0,a_1, ..., a_n).
    In this function we use the functions "top_permutation" and "bottom_permutation" to produce a pair of permutations: one for the 
    top tree and one for bottom tree, of the ternary tree diagram representing g.
    """
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
    This function find the number of leaves in the reduced ternary tree representing an element in F_{3,+}.
    We use the "One-Way Forest Diagrams", [B]. 
    The positive element is written as x_0^{a_0}\cdots x_n^{a_n} for some n, a_0, ..., a_{n-1} (non-negative integers) and a_n (positive integer).
    We have to consider all the non-negative integers 0, 1, 2, 3, 4, ...
    We place carets above non-negative integers for each element appearing in the above expression, starting from the right, that is with x_n.
    We put a ternary caret above the integers n+1, n+2 and n+3 (note the indices are shifted by 1, "traditionally" the caret would be above n, n+1, n+2 
    but for convenience we made this small change). 
    Now we re-number all the non-negative integers and the (n+1)-th point is the root of the caret that we just placed, 
    while n+4 is now n+2, n+5 is n+3, and so on. 
    We continue with the other elements in x_0^{a_0}\cdots x_n^{a_n-1} (again starting from the right) until we finish.
    In this function we cannot store all the non-negative integers, so we create a vector called "integer_interval" with all integers 
    from 0 to max_dimension and for each element in x_0^{a_0}\cdots x_n^{a_n} we remove 2 entries. For example, for x_n 
    we remove the (n+2)-th and (n+3)-th entries. Then if x_k appears in x_0^{a_0}\cdots x_n^{a_n-1} as rightmost element, 
    we remove the (k+2) and (k+3)-th entries of the new vector and continue in the same way.
    Checking where the "holes" in "integer_interval" are will tell us the number of leaves. 
    
    References:
    [B] J. Belk, Thompson's group F. Ph.D. Thesis (Cornell University).  preprint arXiv:0708.3609 (2007).
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
