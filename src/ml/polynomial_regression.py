#https://stackoverflow.com/questions/35491274/split-a-pandas-column-of-lists-into-multiple-columns
#RENDERE VARIABILE m GLOBALE, IN TUTTI I FILE
from typing import List
from xmlrpc.client import Boolean
from src.global_constants.constants import WIDTH_VECTOR
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import PolynomialFeatures


import matplotlib.pyplot as plt

from src.ml.model_manager import ModelManager
plt.style.use("ggplot")
plt.rcParams['figure.figsize'] = (12, 8)

table =pd.read_csv('data.csv')
print(table.head())

m=WIDTH_VECTOR 
exponents = []

class PolynomialRegression(ModelManager):
    def __init__(self, degree: int, test_size: float, shuffle: bool=True):
        super().__init__()
        self.degree = degree
        self.model: PolynomialFeatures = PolynomialFeatures(degree=self.degree)
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

    def mse(self) -> float:
        return mean_squared_error(self.y_test, self.y_pred)

X=table.loc[:,['leaves', *[ 'x'+str(i) for i in range(m)]]]
y=table['orbits']

X_train, X_test, y_train, y_test = split_dataset_train_test(X, y, 0.3)


#degree =1
#----------------------------------------------------------------------------------------#
# Step 2: data preparation

nb_degree = 1

polynomial_features = PolynomialFeatures(degree = nb_degree)

X_TRANSF = polynomial_features.fit_transform(X_train)

#----------------------------------------------------------------------------------------#
# Step 3: define and train a model

model = LinearRegression()

model.fit(X_TRANSF, y_train)


#----------------------------------------------------------------------------------------#
# Step 4: calculate bias and variance on train set

#X_TRANSF_train = polynomial_features.fit_transform(X_train)

y_pred = model.predict(X_TRANSF)

rmse = np.sqrt(mean_squared_error(y_pred,y_train))
r2 = r2_score(y_train,y_pred)

print('Test on training set (degree = 1)')
print('RMSE: ', rmse)
print('R2: ', r2)
# print('polynomial', model)
# print(type(model))

# exit(0)


#----------------------------------------------------------------------------------------#
# Step 5: calculate bias and variance on test set

X_TRANSF_test = polynomial_features.fit_transform(X_test)

y_pred = model.predict(X_TRANSF_test)

rmse = np.sqrt(mean_squared_error(y_test,y_pred))
r2 = r2_score(y_test,y_pred)

print('Test on test set')
print('RMSE: ', rmse)
print('R2: ', r2)



#degree =2
#----------------------------------------------------------------------------------------#
# Step 2: data preparation

nb_degree = 2

polynomial_features = PolynomialFeatures(degree = nb_degree)

X_TRANSF = polynomial_features.fit_transform(X_train)

#----------------------------------------------------------------------------------------#
# Step 3: define and train a model

model = LinearRegression()

model.fit(X_TRANSF, y_train)


#----------------------------------------------------------------------------------------#
# Step 4: calculate bias and variance on train set

#X_TRANSF_train = polynomial_features.fit_transform(X_train)

y_pred = model.predict(X_TRANSF)

rmse = np.sqrt(mean_squared_error(y_pred,y_train))
r2 = r2_score(y_train,y_pred)

print('Test on training set (degree = 2)')
print('RMSE: ', rmse)
print('R2: ', r2)


#----------------------------------------------------------------------------------------#
# Step 5: calculate bias and variance on test set

X_TRANSF_test = polynomial_features.fit_transform(X_test)

y_pred = model.predict(X_TRANSF_test)

rmse = np.sqrt(mean_squared_error(y_test,y_pred))
r2 = r2_score(y_test,y_pred)

print('Test on test set')
print('RMSE: ', rmse)
print('R2: ', r2)




#degree =3
#----------------------------------------------------------------------------------------#
# Step 2: data preparation

nb_degree = 3

polynomial_features = PolynomialFeatures(degree = nb_degree)

X_TRANSF = polynomial_features.fit_transform(X_train)

#----------------------------------------------------------------------------------------#
# Step 3: define and train a model

model = LinearRegression()

model.fit(X_TRANSF, y_train)


#----------------------------------------------------------------------------------------#
# Step 4: calculate bias and variance on train set

#X_TRANSF_train = polynomial_features.fit_transform(X_train)

y_pred = model.predict(X_TRANSF)

rmse = np.sqrt(mean_squared_error(y_pred,y_train))
r2 = r2_score(y_train,y_pred)

print('Test on training set (degree = 3)')
print('RMSE: ', rmse)
print('R2: ', r2)


#----------------------------------------------------------------------------------------#
# Step 5: calculate bias and variance on test set

X_TRANSF_test = polynomial_features.fit_transform(X_test)

y_pred = model.predict(X_TRANSF_test)

rmse = np.sqrt(mean_squared_error(y_test,y_pred))
r2 = r2_score(y_test,y_pred)

print('Test on test set')
print('RMSE: ', rmse)
print('R2: ', r2)

sns.residplot(x=y_test, y=y_pred)
plt.show()

#degree=4
#----------------------------------------------------------------------------------------#
# Step 2: data preparation

nb_degree = 4

polynomial_features = PolynomialFeatures(degree = nb_degree)

X_TRANSF = polynomial_features.fit_transform(X_train)

#----------------------------------------------------------------------------------------#
# Step 3: define and train a model

model = LinearRegression()

model.fit(X_TRANSF, y_train)


#----------------------------------------------------------------------------------------#
# Step 4: calculate bias and variance on train set

#X_TRANSF_train = polynomial_features.fit_transform(X_train)

y_pred = model.predict(X_TRANSF)

rmse = np.sqrt(mean_squared_error(y_pred,y_train))
r2 = r2_score(y_train,y_pred)

print('Test on training set (degree = 4)')
print('RMSE: ', rmse)
print('R2: ', r2)


#----------------------------------------------------------------------------------------#
# Step 5: calculate bias and variance on test set

X_TRANSF_test = polynomial_features.fit_transform(X_test)

y_pred = model.predict(X_TRANSF_test)

rmse = np.sqrt(mean_squared_error(y_test,y_pred))
r2 = r2_score(y_test,y_pred)

print('Test on test set')
print('RMSE: ', rmse)
print('R2: ', r2)


sns.residplot(x=y_test, y=y_pred)
plt.show()




#degree=5
#----------------------------------------------------------------------------------------#
# Step 2: data preparation

nb_degree = 5

polynomial_features = PolynomialFeatures(degree = nb_degree)

X_TRANSF = polynomial_features.fit_transform(X_train)

#----------------------------------------------------------------------------------------#
# Step 3: define and train a model

model = LinearRegression()

model.fit(X_TRANSF, y_train)


#----------------------------------------------------------------------------------------#
# Step 4: calculate bias and variance on train set

#X_TRANSF_train = polynomial_features.fit_transform(X_train)

y_pred = model.predict(X_TRANSF)

rmse = np.sqrt(mean_squared_error(y_pred,y_train))
r2 = r2_score(y_train,y_pred)

print('Test on training set (degree = 5)')
print('RMSE: ', rmse)
print('R2: ', r2)


#----------------------------------------------------------------------------------------#
# Step 5: calculate bias and variance on test set

X_TRANSF_test = polynomial_features.fit_transform(X_test)

y_pred = model.predict(X_TRANSF_test)

rmse = np.sqrt(mean_squared_error(y_test,y_pred))
r2 = r2_score(y_test,y_pred)

print('Test on test set')
print('RMSE: ', rmse)
print('R2: ', r2)


sns.residplot(x=y_test, y=y_pred)
plt.show()



#degree=6
#----------------------------------------------------------------------------------------#
# Step 2: data preparation

nb_degree = 6

polynomial_features = PolynomialFeatures(degree = nb_degree)

X_TRANSF = polynomial_features.fit_transform(X_train)

#----------------------------------------------------------------------------------------#
# Step 3: define and train a model

model = LinearRegression()

model.fit(X_TRANSF, y_train)


#----------------------------------------------------------------------------------------#
# Step 4: calculate bias and variance on train set

#X_TRANSF_train = polynomial_features.fit_transform(X_train)

y_pred = model.predict(X_TRANSF)

rmse = np.sqrt(mean_squared_error(y_pred,y_train))
r2 = r2_score(y_train,y_pred)

print('Test on training set (degree = 6)')
print('RMSE: ', rmse)
print('R2: ', r2)


#----------------------------------------------------------------------------------------#
# Step 5: calculate bias and variance on test set

X_TRANSF_test = polynomial_features.fit_transform(X_test)

y_pred = model.predict(X_TRANSF_test)

rmse = np.sqrt(mean_squared_error(y_test,y_pred))
r2 = r2_score(y_test,y_pred)

print('Test on test set')
print('RMSE: ', rmse)
print('R2: ', r2)


sns.residplot(x=y_test, y=y_pred)
plt.show()


exit(0)
y_pred = model.predict(X_TRANSF)



error: float = mse(y_test, y_pred)

print("ERROR = ", error)

sns.residplot(x=y_test, y=y_pred)
plt.show()