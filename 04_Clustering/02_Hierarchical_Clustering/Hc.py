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
dataset.iloc[:, [2,3]].values
