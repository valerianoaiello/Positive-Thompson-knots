import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import skew

import matplotlib.pyplot as plt
plt.style.use("ggplot")
plt.rcParams['figure.figsize'] = (12, 8)

table =pd.read_csv('data.csv')
#print(table.head())

#table.info()

#non lo stampa :-(
#sns.pairplot(table,x_vars=['leaves', 'vector'], y_vars='orbits', height=10, aspect=.7)


from sklearn.linear_model import LinearRegression
X=table[['leaves', 'vector']]
y=table.orbits

lm1=LinearRegression()
lm1.fit(X,y)
print(lm1.intercept_)
print(lm1.coef_)