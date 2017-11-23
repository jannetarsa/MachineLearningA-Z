# -*- coding: utf-8 -*-
#Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
"""
Created on Mon Nov 20 22:03:44 2017

@author: janne_000
"""
dataset = pd.read_csv('Data.csv')
# take all values except last column
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values