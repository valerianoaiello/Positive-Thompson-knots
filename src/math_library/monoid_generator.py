import numpy as np


class MonoidElementGenerator:
    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

    def generate_monoid_elements(self) -> np.ndarray:
        admissible_exponents = list(range(self.height))

        repeated_admissible_exponents = [admissible_exponents]*self.width

        elements_matrix = np.array(np.meshgrid(*repeated_admissible_exponents)).T.reshape(-1, self.width)

        return elements_matrix

    def random_generate_monoid_elements(self, number_of_elements: int) -> np.ndarray:
        elements_matrix: np.ndarray = np.random.randint(
            self.height, size=(number_of_elements, self.width))

        return elements_matrix


if __name__ == '__main__':
    print(MonoidElementGenerator(height=5, width=10).generate_monoid_elements())
