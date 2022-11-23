import numpy as np
from sympy.combinatorics import Permutation

"""
v = (v_1, v_2, ..., v_n)
0 <= v_i < m, v_i in N, for every i
"""


def __bottom_permutation(n: int) -> np.ndarray:
    """
    This function computes the permutation associated with the bottom tree of a positive Thompson element
    n must be an odd number and the permutation acts on {0,1,...,n}
    """
    if n % 2 == 0:
        print('The number is even')
        exit(0)
    if n == 1:
        p = Permutation(0, 1)
    elif n == 3:
        p = Permutation(0, 2)(1, 3)
    else:
        q = Permutation(0, 2)
        m = int((n - 3)/2)
        for i in range(m):
            q = Permutation(q(2*i + 1, 2*i + 4))
        p = Permutation(q(n - 2, n))

    return np.array(p.array_form)


def __top_permutation(n: int, v: np.ndarray) -> np.ndarray:
    """
    This function computes the permutation associated with the top tree of a positive Thompson element.
    Arg:
    - n is odd number and the permutation acts on {0,1,...,n}
    """
    if n % 2 == 0:
        print('The number is even')
        exit(0)
    if n == 1:
        p = np.array([1, 0])
    elif n == 3:
        p = np.array([2, 3, 0, 1])
    elif n >= 5 and not np.any(v):
        p = __bottom_permutation(n)
    else:
        z = np.nonzero(v)[0]
        k = len(z)
        a = z[k-1]

        v_prime = v.copy()
        v_prime[a] = v_prime[a]-1

        w = __top_permutation(n-2, v_prime)
        p = np.zeros(n+1).astype(int)
        for i in range(n-1):
            if i <= a and w[i] <= a:
                p[i] = w[i]
            elif i <= a and w[i] == a + 1:
                p[i] = w[i] + 1
            elif i <= a and w[i] >= a + 2:
                p[i] = w[i] + 2
            elif i >= a + 2 and w[i] >= a + 2:
                p[i + 2] = w[i] + 2
            elif i >= a + 2 and w[i] <= a:
                p[i + 2] = w[i]
            elif i >= a + 2 and w[i] == a + 1:
                p[i + 2] = a + 2
            elif i == a + 1 and w[i] >= a + 2:
                p[i + 1] = w[i] + 2
            elif i == a + 1 and w[i] <= a:
                p[i + 1] = w[i]
        p[a + 1] = a + 3
        p[a + 3] = a + 1
    return p


def whole_permutation(n: int, v: np.ndarray) -> np.ndarray:
    p = __top_permutation(n, v)
    q = __bottom_permutation(n)

    tot = []

    for i in range(n):
        l: list = []
        if i not in [item for sublist in tot for item in sublist]:
            while True:
                if p[i] not in l:
                    l.append(p[i])
                    i = p[i]
                    if q[i] not in l:
                        l.append(q[i])
                        i = q[i]
                    else:
                        break
                else:
                    break
            tot.append(l)
    return tot

# this function find the number of leaves in the reduced ternary tree representing an element in F_{3,+}


def number_of_leaves(v: np.ndarray) -> int:
    z = np.nonzero(v)[0]
    k = len(z)
    m = 1000
    w = np.array(list(range(m)))
    u = w.copy()
    for i in range(k - 1, -1, -1):
        for j in range(v[z[i]]):
            w = np.delete(w, z[i]+1)
            w = np.delete(w, z[i]+1)
    n = 0
    for i in range(len(w)-1):
        if w[i + 1] - w[i] >= 2:
            n = w[i + 1]
    if n % 2 == 1:
        n = n + 2
    else:
        n = n + 1
    return n
