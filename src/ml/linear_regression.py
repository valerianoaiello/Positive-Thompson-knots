#https://stackoverflow.com/questions/35491274/split-a-pandas-column-of-lists-into-multiple-columns
#RENDERE VARIABILE m GLOBALE, IN TUTTI I FILE
from typing import List
from xmlrpc.client import Boolean
from constants import WIDTH_VECTOR
import tree
from unicodedata import name
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import skew
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sympy import variations
plt.style.use("ggplot")
plt.rcParams['figure.figsize'] = (12, 8)

table =pd.read_csv('data.csv')
print(table.head())

m=WIDTH_VECTOR 
exponents = []

def split_dataset_train_test(X: pd.DataFrame, y: pd.DataFrame, test_size: float, shuffle: Boolean=True) -> List[pd.DataFrame]:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, shuffle=shuffle)
    return X_train, X_test, y_train, y_test

def mse(y_test: pd.DataFrame, y_pred: pd.DataFrame) -> float:
    return mean_squared_error(y_test, y_pred)

X=table.loc[:,['leaves', *[ 'x'+str(i) for i in range(m)]]]
y=table['orbits']

X_train, X_test, y_train, y_test = split_dataset_train_test(X, y, 0.3)

lm1=LinearRegression()
lm1.fit(X_train,y_train)
print(lm1.intercept_)
print(lm1.coef_)

y_pred = lm1.predict(X_test)

error: float = mse(y_test, y_pred)

print("ERROR = ", error)

sns.residplot(x=y_test, y=y_pred)
plt.show()