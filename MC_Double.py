# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 21:58:53 2023

@author: rjfch
"""

# monte_carlo_double.py
import numpy as np

def MonteCarlo_double(f, g, x0, x1, y0, y1, n):
    """
    Monte Carlo integration of f over a domain g>=0, embedded
    in a rectangle [x0,x1] -by- [y0,y1]. n^2 is the number of
    random points.
    """
    # Draw n^2 random points in the rectangle
    x = np.random.uniform(x0, x1, n)
    y = np.random.uniform(y0, y1, n)
    # Compute sum of f values inside the integration domain
    f_mean = 0
    num_inside = 0   # number of x,y points inside domain (g>=0)
    for i in range(len(x)):
        for j in range(len(y)):
            if g(x[i], y[j]) >= 0:
                num_inside = num_inside + 1
                f_mean = f_mean + f(x[i], y[j])
    f_mean = f_mean / num_inside
    area = num_inside / (n**2) * (x1 - x0) * (y1 - y0)
    return area * f_mean
   