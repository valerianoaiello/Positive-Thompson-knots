#https://stackoverflow.com/questions/35491274/split-a-pandas-column-of-lists-into-multiple-columns
#RENDERE VARIABILE m GLOBALE, IN TUTTI I FILE

from unicodedata import name
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import skew
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
plt.style.use("ggplot")
plt.rcParams['figure.figsize'] = (12, 8)

table =pd.read_csv('data.csv')
print(table.head())

m=7#Make this global
exponents = []

table2 = pd.DataFrame(table) 
print(table2.head())
print(table2.dtypes)
print(table2.info())

table.drop(columns=['bottom_permutation','top_permutation','permutation'], inplace=True)

print(table.head())

l=table['vector'].to_list()
l=[(i.strip("[]").split(" ")) for i in l]
l2=table['orbits']
table2 = pd.DataFrame(l, columns=['x'+str(i) for i in range(m)])
table2['orbits']=table['orbits']
table2.insert(0, "leaves", table['leaves'], True)
print(table2.head(8))

table2.to_csv('data_bis.csv', index=False)


#print(table.head())
#table.info()

#non lo stampa :-(
#sns.pairplot(table2,x_vars=["leaves"], y_vars="leaves", height=10, aspect=.7)
#sns.pairplot(table,x_vars=['leaves', 'x0', 'x1','x2','x3','x4','x5'], y_vars='orbits', height=10, aspect=.7)
#plt.savefig(fname='prova.jpg')

X=table2.loc[:,['leaves','x0', 'x1','x2','x3','x4','x5','x6']]
y=table2['orbits']
lm1=LinearRegression()
lm1.fit(X,y)
print(lm1.intercept_)
print(lm1.coef_)

w=zip(['leaves','x0', 'x1','x2','x3','x4','x5','x6'], lm1.coef_)
list(w)
print(w)