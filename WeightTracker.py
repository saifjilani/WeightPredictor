#!/usr/bin/env python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

data = pd.read_table('https://onlinecourses.science.psu.edu/stat501/sites/onlinecourses.science.psu.edu.stat501/files/data/bldgstories.txt', delim_whitespace=True)
X = pd.DataFrame(data['STORIES'])
y = pd.DataFrame(data['HGHT'])
# we want to pass in our variables as DataFrames

# # establish what kind of modeling technique we will be using
# lm = linear_model.LinearRegression()

# # fit our model!
# model = lm.fit(X, y)

# # make predictions from our X variable using our model!
# predictions = lm.predict(X)


