# -*- coding: utf-8 -*-

# Simple linear regression

#Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
"""
Created on Mon Nov 20 22:03:44 2017

@author: janne_000
"""
dataset = pd.read_csv('Salary_Data.csv')
# take all values except last column
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values


# Splitting the data into the training and test data sets
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Feature scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""
