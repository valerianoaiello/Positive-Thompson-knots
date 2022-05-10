#https://stackoverflow.com/questions/35491274/split-a-pandas-column-of-lists-into-multiple-columns
#RENDERE VARIABILE m GLOBALE, IN TUTTI I FILE

from unicodedata import name
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import skew
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
plt.style.use("ggplot")
plt.rcParams['figure.figsize'] = (12, 8)

table =pd.read_csv('data.csv')
print(table.head())

m=6#Make this global
exponents = []

table2 = pd.DataFrame(table) 
print(table2.head())
print(table2.dtypes)
print(table2.info())

l=table['vector'].to_list()
l=[i.split(" ") for i in l]

table2 = pd.DataFrame(l, columns=['x'+str(i) for i in range(m)])


print(table2.head())
exit(0)

print(table2.dtypes)
print(table2.info())

d = {'col1': [[1, 2],[3, 4]]}

df = pd.DataFrame(data=d)
df2 = pd.DataFrame(df['col1'].to_list(), columns=['a','b'])

print(df)
print(df2)


table.drop(columns=['bottom_permutation','top_permutation','permutation'], inplace=True)
print(table.head())
#table.info()

#non lo stampa :-(
#sns.pairplot(table,x_vars=['leaves'], y_vars='orbits', height=10, aspect=.7)
#plt.savefig(fname='prova.jpg')

X=table2[['leaves','vector']]
y=table2.orbits

lm1=LinearRegression()
lm1.fit(X,y)
print(lm1.intercept_)
print(lm1.coef_)