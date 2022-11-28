# Positive Thompson Knots

## The Thompson group $F$ and the Brown-Thompson group $F_3$
The Thompson group $F$ and the Brown-Thompson group $F_3$ admit infinite presentations, namely 
<p align="center">
$\langle y_0, y_1, ...| y_n y_l = y_l y_{n+1}$ for all $l < n\rangle$ and
$\langle x_0, x_1, ...| x_n x_l = x_l x_{n+2}$ for all $l < n\rangle$
</p>
respectively [CFP, B, Brown].

Every element of $F_3$ can be represented by pairs of ternary trees with the same number of leaves and such pairs are called ternary tree diagrams. 
The representation is non-unique, but there exists a unique minimal representive, that is with minimal number of leaves.

Both contain interesting monoids. The positive monoid $F_+$ of $F$ is the one generated by $y_0$, $y_1$, ...
Similarly, the positive monoid $F_{3,+}$ of $F_3$ is  generated by by $x_0$, $x_1$, ...
The elements of these monoids are called positive.

Every element positive element of $F_3$ can be written uniquely as $x_0^{a_0}\cdots x_n^{a_n}$ for some $n$, $a_0$, ..., $a_{n-1}$ in $\mathbb{N} \cup \{0\}$ and $a_n\in \mathbb{N}$. We call $n$ the width and $\max_{i}a_i$ the height of the element.

There is a natural injection of $F$ into $F_3$ which is obtained by mapping $y_i$ to $x_{2i}$ for all $i$.
Correspongly, we have an injection of $F_+$ into $F_{3,+}$.

## Jones construction of knots
In 2014 Vaughan Jones defined a method to construct link from elements of the Thompson group $F$, which was later extended to the Brown-Thompson group $F_3$, [Jo14, Jo18]. Both $F$ and $F_3$ are just as a good as the braid groups at producing links. More precisely, for every link $L$ there exists an element $g$ such that its closure $\mathcal{L}(g)$ is equivalent to $L$.

## Thompson Permutations
It is possible to associate permutations to braids in a natural way, where the number of orbits (or cycles in the cycle decomposition) of the permutation is equal to the number of connected components of the link.
We define a method to associate a permutation $\mathcal{P}(g)$ to each element $g$ of the Brown-Thompson group in such a way that its number of orbits coincides with the number of connected components of $\mathcal{L}(g)$. We call $\mathcal{P}(g)$ the Thompson permutation associated with $g$.

## Code
The main files are monoid_elements_generator.py and positive_bt_permutations.py.

### monoid_elements_generator.py
Consider two positive integers $h$ and $w$. 
In this file we introduce a class called MonoidElementsGenerator, which contains two methods: generate_monoid_elements and random_generate_monoid_elements.
The former produces all positive elements in $F_3$ with height at most $h$ and width at most $w$.
The latter takes a positive integer $n$ as an argument and produces $n$ random positive elements with height at most $h$ and width at most $w$.

### positive_bt_permutations.py
In this file we present a function, called "whole_permutation" that produces $\mathcal{P}(g)$ for positives elements. It receives 
a natural number $k$ and a numpy vector $v=(a_0,a_1, ..., a_n)$ as an input and returns a permutations as a list (the elements of the list are the distict cycles of the permutation). The number $k$ is the number of leaves in the minimal representative in terms of ternary tree diagrams, while $v$ represents
the exponents that appear in the description the element as  $x_0^{a_0}\cdots x_n^{a_n}$.

We explored the permutations of elements with selected values of width and height. The results are stored in csv files and presented in [AiIo].


## Bibliography
[AiIo] V. Aiello, S. Iovieno, A computational study of the number of connected components of positive Thompson links.

[B] J. Belk, Thompson's group F. Ph.D. Thesis (Cornell University).  preprint arXiv:0708.3609 (2007).

[Brown] K. S. Brown, Finiteness properties of groups. Proceedings of the Northwestern conference on cohomology of groups (Evanston, Ill., 1985). J. Pure Appl. Algebra 44 (1987), no. 1-3, 45-75.

[CFP]
J.W. Cannon, W.J Floyd,   W.R. Parry, 
Introductory notes on Richard Thompson's groups.
L'Enseignement  Mathématique
42 (1996): 215-256


[Jo14] V.F.R. Jones, Some unitary representations of Thompson's groups $F$ and $T$. J. Comb. Algebra 1 (2017), 1-44.

[Jo18] V.F.R. Jones, On the construction of knots and links from Thompson's groups.  In: Adams C. et al. (eds) Knots, Low-Dimensional Topology and Applications. KNOTS16 2016. Springer Proceedings in Mathematics \& Statistics, vol 284. Springer, Cham.
