#https://stackoverflow.com/questions/35491274/split-a-pandas-column-of-lists-into-multiple-columns
 
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
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import model_selection
import matplotlib.pyplot as plt
from sympy import variations
plt.style.use("ggplot")
plt.rcParams['figure.figsize'] = (12, 8)

table =pd.read_csv('data.csv')
print(table.head())
m=WIDTH_VECTOR 


def split_dataset_train_test(X: pd.DataFrame, y: pd.DataFrame, test_size: float, shuffle: Boolean=True) -> List[pd.DataFrame]:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, shuffle=shuffle)
    return X_train, X_test, y_train, y_test

def mse(y_test: pd.DataFrame, y_pred: pd.DataFrame) -> float:
    return mean_squared_error(y_test, y_pred)

X=table.loc[:,['leaves', *[ 'x'+str(i) for i in range(m)]]]
y=table['orbits']

X_train, X_test, y_train, y_test = split_dataset_train_test(X, y, 0.3)

# Logistic regression


X=table.loc[:,['leaves', *[ 'x'+str(i) for i in range(m)]]]
y=table['orbits']

X_train, X_test, y_train, y_test = split_dataset_train_test(X, y, 0.3)


lm2 = LogisticRegression(multi_class='ovr', solver='liblinear')
lm2.fit(X_train, y_train)


y_pred = lm2.predict(X_test)

error: float = mse(y_test, y_pred)

print("ERROR = ", error)

sns.residplot(x=y_test, y=y_pred)
plt.show()
exit(0)

lm2 = LogisticRegression()
lm2 = LogisticRegression(random_state=0).fit(X_train,y_train)
print(lm2)
  

















def logistic_function(x):
    return 1/(1+np.exp(-x))

def compute_cost(theta, x, y):
    m=len(y)
    y_pred=logistic_function(np.dot(x,theta))
    error=(y*np.log(y_pred))+(1-y)*np.log(1-y_pred)
    cost=-1/m*sum(error)
    gradient=1/m*np.dot(x.transpose(),(y_pred-y))
    return cost[0], gradient

mean_scores=np.mean(scores,axis=0)
std_scores=np.std(scores,axis=0)
scores=(scores-mean_scores)/std_scores

rows=scores.shape[0]
cols=scores.shape[1]

X=np.append(np.ones((rows,1)),scores, axis=1)
y=results.reshape(rows,1)

theta_init=np.zeros((cols+1,1))
cost, gradient= compute_cost(theta_init, X, y)

print('Cost at initialization', cost)
print('Gradient at initialization', gradient)

def gradient_descent(x,y, theta, alpha, iterations):
    costs=[]
    for i in range(iterations):
        cost, gradient=compute_cost(theta, x, y)
        theta-= (alpha*gradient)
        costs.append(cost)
    return theta, costs

theta, costs= gradient_descent(X,y,theta_init, 1, 200)

print('Theta after running gradient descent: ', theta)
print('Resulting cost: ', costs[-1])


plt.plot(costs)
plt.xlabel("Iterations")
plt.ylabel("$J(\Theta)$")
plt.title("Values of cost function over itterations of gradient descent")


ax=sns.scatterplot(x=X[passed[:,0],1], y=X[passed[:, 0],2], marker="^", color= 'green', s=60)
sns.scatterplot(x=X[failed[:, 0],1], y=X[failed[:,0],2], marker="X", color= 'red', s=60)
ax.legend(['Passed','Failed'])
ax.set(xlabel="DMV Written Test 1 scores", ylabel="DMV Written test 2 scores")

x_boundary=np.array([np.min(X[:, 1]),np.max(X[:,1])])
y_boundary= - (theta[0]+theta[1]*x_boundary)/theta[0]

sns.lineplot(x=x_boundary, y=y_boundary, color="blue")
plt.show();

def predict(theta,x):
    results=logistic_function(x.dot(theta))
#    results=x.dot(theta)

    return results >0

p= predict(theta,X)
print("Training accuracy", sum(p==y)[0],"%")






