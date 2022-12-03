import numpy as np

"""
An element of F_{3,+} can be written uniquely as x_0^{a_0}\cdots x_n^{a_n} for some n, a_0, ..., a_{n-1} in N \cup {0} and 
a_n in N,  which we may represent as a vector v = (a_0,a_1, ..., a_n).
The method generate_monoid_elements returns all the vectors in R^width whose components are between 0 and height.
For this reason we add some zeros at the end of the vectors v = (a_0,a_1, ..., a_n) so that they belong to R^width.
The idea is the following: we first create a vector called admissible_exponents with entries from 0, to height in ascending order.
Then we create a matrix "repeated_admissible_exponents" in M_{height, width}(Z), whose columns are all equal to "admissible_exponents".
Finally, we obtain all the desired vectors by selecting an entry in "repeated_admissible_exponents" per column.

The method random_generate_monoid_elements picks n random vectors in R^width whose components are between 0 and height.
"""
class MonoidElementsGenerator:
    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

    def generate_monoid_elements(self) -> np.ndarray:
        admissible_exponents = list(range(self.height + 1))

        repeated_admissible_exponents = [admissible_exponents]*self.width

        elements_matrix = np.array(np.meshgrid(*repeated_admissible_exponents)).T.reshape(-1, self.width)

        return elements_matrix

    def random_generate_monoid_elements(self, number_of_elements: int) -> np.ndarray:
        elements_matrix: np.ndarray = np.random.randint(
            self.height + 1, size=(number_of_elements, self.width))

        return elements_matrix


if __name__ == '__main__':
    print(MonoidElementsGenerator(height=2, width=2).generate_monoid_elements())
