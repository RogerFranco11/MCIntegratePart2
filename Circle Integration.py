# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 21:59:53 2023

@author: rjfch
"""

# circle_integration.py
import math
from MC_Double import MonteCarlo_double

def circle_g(x, y):
    return 1.5**2 - x**2 - y**2

def f(x, y):
    return 1  # Constant function, as we are just calculating area

if __name__ == "__main__":
    x0, x1 = -1.5, 1.5
    y0, y1 = -1.5, 1.5
    n = 10000

    circle_area = MonteCarlo_double(f, circle_g, x0, x1, y0, y1, n)
    print(f"The area of the circle with a radius of 1.5 is approximately: {circle_area}")