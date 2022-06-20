from abc import ABC, abstractmethod
import pandas as pd

class ModelManager(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def split_dataset_train_test(self, X: pd.DataFrame, y: pd.DataFrame) -> None:
        pass

    @abstractmethod
    def regression(self) -> None:
        pass

    @abstractmethod
    def mse(self) -> float:
        pass