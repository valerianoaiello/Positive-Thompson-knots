import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from constants import WIDTH_VECTOR

plt.style.use("ggplot")
plt.rcParams['figure.figsize'] = (12, 8)

table =pd.read_csv('data.csv')
print(table.head())

m=WIDTH_VECTOR 
exponents = []
class LinearRegression:
    def __init__(self, test_size: float, shuffle: bool=True) -> None:
        self.model: LinearRegression = LinearRegression()
        self.intercept = None
        self.coefficients = None
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
        self.y_pred = None
        self.test_size = test_size
        self.shuffle = shuffle

    def split_dataset_train_test(self, X: pd.DataFrame, y: pd.DataFrame) -> None:
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, 
            y, 
            test_size=self.test_size, 
            shuffle=self.shuffle
            )

    def linear_regression(self) -> None:
        self.model.fit(self.X_train, self.y_train)
        self.intercept = self.model.intercept_
        self.coefficients = self.model.coef_
        self.y_pred = self.model.predict(self.X_test)

    def mse(self) -> float:
        return mean_squared_error(self.y_test, self.y_pred)

X=table.loc[:,['leaves', *[ 'x'+str(i) for i in range(m)]]]
y=table['orbits']