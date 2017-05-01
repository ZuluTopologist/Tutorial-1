# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 11:19:53 2017

@author: Inxeba lasemaQadini
"""

import numpy
import math
from matplotlib import pyplot as plt


def myCos_Integral(N):

      for n in N:
       dx=(math.pi/2)/n
       x=numpy.linspace(0,math.pi/2,n)
       y=numpy.cos(x)
       integral=y.sum()*dx
       err=numpy.absolute(1-integral)
       return err

NoOfPoints=[10,30,100,300,1000]
Error=myCos_Integral(NoOfPoints)
plt.plot(NoOfPoints,Error)
 

