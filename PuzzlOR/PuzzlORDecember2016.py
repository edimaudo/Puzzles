 #PuzzlOR December 2016 - Galaxy on fire

# tenata
import numpy as np
from sklearn import linear_model
import pandas as pd

# Cargo, weapon, equipment
inputs = np.array([[25, 2, 6],
                 [350, 0, 8],
                 [38, 4, 5],
                 [28, 2, 8],
                 [45, 2, 7],
                 [80, 2, 8],
                 [60, 4, 6],
                 [50, 3,  5],
                 [65, 2,  7],
                 [30, 2, 6]])
costs = np.array([51975, 168900, 235600, 171900, 150000, 250000, 294900, 100100, 125400, 72500])
costs = costs.reshape(10,1)

data = np.concatenate((inputs,costs),axis=1)

lmodel = linear_model.LinearRegression(fit_intercept = False, normalize=True)
lmodel.fit(inputs,costs)
print(lmodel.coef_)
print((costs - np.dot(inputs,lmodel.coef_.T)))
print("")
print( (costs - np.dot(inputs,lmodel.coef_.T)).min())
