# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 22:05:28 2023

@author: rjfch
"""

import numpy as np 
import MCIntegratePart2 as mc


def f(x):
    return (x**2)
print(f(.5))

n = 10
x0 = 0
x1 = 1
y0 = 0
y1 = 1
ans = mc.MCinteg(f, x0, x1, y0, y1, n)
print(ans)
