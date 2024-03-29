# -*- coding: utf-8 -*-
"""Q3_test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dWm-EWFDEwI15WbGIT0_bUIrxolF7Z1G
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from linearRegression.linear_regression import LinearRegression
from os import path
import os

N=60
x = np.array([i*np.pi/180 for i in range(60,300,2)])
np.random.seed(10)
y = 3*x + 8 + np.random.normal(0,3,len(x)) 


y=pd.Series(y)
LR = LinearRegression(fit_intercept=True)
LR.fit_gradient_descent(pd.DataFrame(x), y, batch_size=40, num_iters=10, lr=0.01)
LR.plot_surface(pd.Series(x),y,LR.all_coef.iloc[0],LR.all_coef.iloc[1])
LR.plot_line_fit(pd.Series(x),y,LR.all_coef.iloc[0],LR.all_coef.iloc[1])
LR.plot_contour(pd.Series(x),y,LR.all_coef.iloc[0],LR.all_coef.iloc[1])
