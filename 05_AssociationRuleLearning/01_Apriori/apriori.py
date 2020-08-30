# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 15:48:45 2019

@author: Idur
"""

# Association Rule Learning
# Apriori

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the Dataset
dataset = pd.read_csv("Market_Basket_Optimisation.csv", header = None)

transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i, j]) for j in range(0, 20)])
    
# Training the Apriori on the dataset
#from apyori import apriori
from apyori import apriori
#rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)

# Visualising the results
results = list(rules)