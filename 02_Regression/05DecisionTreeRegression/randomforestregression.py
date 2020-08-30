# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 22:01:00 2019

@author: Idur
"""

# Random Forest Regression

# Polynomial Regression
# Import the dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Imorting the Dataset

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Spliting the dataset into the Training set and Test set
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
Note : no need to create Training set and Test set
"""
# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
y_test = sc_X.transoform(X_test)
Note : no need to Feature Scaling
"""
# Fitting the Random Forest Regression to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=300, random_state = 0)
regressor.fit(X, y)
# Predicting a new result 
y_pred = regressor.predict(6.5)

# Visulising the Random Forest Regression results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (Random Forest Regression Model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

