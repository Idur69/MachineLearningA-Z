# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 22:51:56 2019

@author: Idur
"""

#  Polynomial, SupportVector, DecisionTree, RandomForest Regressions 
# Importing the libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


# Importing the data from csv file
dataset = pd.read_csv("Position_Salaries.csv")
# we need to split the data into features(X) and labels(y)
# here X Independent variables and y Dependent variables
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, -1].values

'''
# Next split the data into trainset and testset
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_satate = 0)

# Feature scalling 
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
y_test = sc_X.transform(y_test)
'''
# Fitting the Linear resgression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Fitting the Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

# Visulaising the Linear regression to the results
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title("Truth or Bluff (Linear Regression)")
plt.xlabel("Position Levels")
plt.ylabel("Salaray")
plt.show()

# Visualising the Polynomial regression results

X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color = "red")
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
plt.title("Truth or Bluff (Polynomial Regression)")
plt.xlabel("Position Levels")
plt.ylabel("Salaray")
plt.show()


# Predicting the new result with linear resgression
lin_reg.predict(6.5)

# Ppedicting the new result with Polynomial Regression
lin_reg_2.predict(poly_reg.fit_transform(6.5))

# 


