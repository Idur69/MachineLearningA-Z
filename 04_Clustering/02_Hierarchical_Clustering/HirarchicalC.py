# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 22:37:20 2019

@author: Idur
"""

# Hierarchical Clustering

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the mall dataset
dataset = pd.read_csv("Mall_Customers.csv")
X = dataset.iloc[:, [3,4]].values

# Using the dendrogram to find the optimal number of cluster
import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
plt.title("Dendrogram")
plt.xlabel("Customers")
plt.ylabel("Euclidean distances")
plt.show()

# Fitting the hierarchical clustering to the mall dataset
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 5, affinity = "euclidean", linkage = "ward")
y_hc = hc.fit_predict(X)

# Visualising the Clusters
plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s =100, c = 'red', label = 'carefull') # high income and low spending score
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s =100, c = 'blue', label = 'Standard') # average income and avg spending score
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s =100, c = 'green', label = 'Target') # high income and high spending score
plt.scatter(X[y_hc == 3, 0], X[y_hc == 3, 1], s =100, c = 'cyan', label = 'Careless') # low income and high spending score
plt.scatter(X[y_hc == 4, 0], X[y_hc == 4, 1], s =100, c = 'magenta', label = 'Sensible') # low income and low spending score
plt.title("Cluster of Customers")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.show()
