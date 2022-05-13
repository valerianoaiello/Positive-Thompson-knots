#https://stackoverflow.com/questions/35491274/split-a-pandas-column-of-lists-into-multiple-columns
#RENDERE VARIABILE m GLOBALE, IN TUTTI I FILE
import tree
from unicodedata import name
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import skew
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sympy import variations
plt.style.use("ggplot")
plt.rcParams['figure.figsize'] = (12, 8)

table =pd.read_csv('data.csv')#.set_index('leaves')
print(table.head())

m=7#Make this global
exponents = []
  
#non lo stampa :-(
# 
# 
#X=table.loc[:,['leaves','x0', 'x1','x2','x3','x4','x5','x6']]
X=table.loc[:,['leaves','x0', 'x1','x2','x3','x4','x5','x6','x7']]
y=table['orbits']
lm1=LinearRegression()
lm1.fit(X,y)
print(lm1.intercept_)
print(lm1.coef_)

vv=np.array([1, 2, 3,4,5,6,7,0])
n=tree.number_leaves_ternary(vv)
vector=np.array([n,1, 2, 3,4,5,6,7,0])
#input('Insert the exponents of x0, x1 x2 x3 x4 x5 x6')
number_pred = np.dot(lm1.coef_,vector)
print('prediction:', number_pred)
print('real value:', len(tree.whole_permutation(tree.number_leaves_ternary(vector),vector)))

exit(0)

sns.pairplot(table,x_vars=['leaves', 'x0', 'x1','x2','x3','x4','x5'], y_vars="orbits", height=10, aspect=.7)
plt.savefig(fname='prova.jpg')

y=table['orbits']
lm1=LinearRegression()
lm1.fit(X,y)
print(lm1.intercept_)
print(lm1.coef_)

#tablecomponents = sns.load_dataset("table")
plt.plot(table[leaves], table['x0'])
plt.savefig(fname='prova.jpg')


#plt.show()
#sns.pairplot(table,x_vars=['leaves', 'x0', 'x1','x2','x3','x4','x5'], y_vars='orbits', height=10, aspect=.7)
plt.savefig(fname='prova.jpg')

X=table2.loc[:,['leaves','x0', 'x1','x2','x3','x4','x5','x6']]
y=table2['orbits']
lm1=LinearRegression()
lm1.fit(X,y)
print(lm1.intercept_)
print(lm1.coef_)

w=zip(['leaves','x0', 'x1','x2','x3','x4','x5','x6'], lm1.coef_)
list(w)
print(type(lm1.coef_))
print(lm1.coef_.shape)
vv=np.array([1, 2, 3,4,5,6,7])
n=tree.number_leaves_ternary(vv)
vector=np.array([n,1, 2, 3,4,5,6,7])
#input('Insert the exponents of x0, x1 x2 x3 x4 x5 x6')
number_pred = np.dot(lm1.coef_,vector)
print('prediction:', number_pred)
print('real value:', len(tree.whole_permutation(tree.number_leaves_ternary(vector),vector)))

lm1_preds=lm1.predict(X[['leaves','x0', 'x1','x2','x3','x4','x5','x6']])
