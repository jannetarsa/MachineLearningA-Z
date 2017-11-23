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
X = dataset.iloc[:, :-1].values