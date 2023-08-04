# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 22:13:31 2023

@author: rjfch
"""

def MCinteg(f, x0, x1, y0, y1, n):
    from MC_Double import MonteCarlo_double
    import numpy as np 
    """
    
    
    Parameters
    ----------
    f: TYPE float function 
       DESCRIPTION. function to be integrated
    x0: TYPE float
        DESCRIPTION. on the x-axis where to start integral 
    x1: TYPE float 
        DESCRIPTION. on the x-axis where to stop integral
    y0: TYPE Float
        DESCRIPTION. bottom of the rectangle, y0=0
    y1: TYPE float 
        DESCRIPTION. type of the rectangle 
    n: TYPE Integer
       DESCRIPTION. n**2 points in rectangle 
       
    Returns
    -------
    Integral of f from x0 to x1 
    
    """
    x = np.random.random(n)*(x1-x0)+x0
    y = np.random.random(n)*(y1-y0)+y0
    
    areaCount = 0
    
    for i in range(len(x)):
        xVal = x[i]
        for j in range(len(y)):
            yVal = y[j]
            if f(xVal) < yVal: areaCount +=1
            
    area = areaCount/(n**2)*(x1-x0)*(y1-y0)
    return area 
if __name__ == "__main__":
    
     def f(x):
        return x 
     x0=0
     x1=1
     y0=0
     y1=1
     n=500
     
     area = MCinteg(f, x0, x1, y0, y1, n)
     print(area)
    
    
    