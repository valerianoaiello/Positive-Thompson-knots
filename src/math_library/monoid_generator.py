import numpy as np

class MonoidGenerator:
    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

    def generate_monoid_elements(self) -> np.ndarray:
        v = list(range(self.height))
        l = [v for i in range(self.width)]

        w = np.array(np.meshgrid(*l)).T.reshape(-1, self.width)
        w = w[(w[:, 0] != 0) | (w[:, 1] != 0)]

        return w

    def random_generate_monoid_elements(self, vector_number: int) -> np.ndarray:
        vector_matrix: np.ndarray = np.random.randint(
            self.height, size=(vector_number, self.width))
        vector_matrix = vector_matrix[(
            vector_matrix[:, 0] != 0) | (vector_matrix[:, 1] != 0)]
        return vector_matrix

if __name__ == '__main__':
    print(MonoidGenerator.generate_monoid_elements())