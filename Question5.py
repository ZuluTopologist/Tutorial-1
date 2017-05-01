# -*- coding: utf-8 -*-
"""
Created on Mon May 01 11:05:08 2017

@author: Inxeba lasemaQadini
"""

import numpy
import math


N=[11,30,100,300,1000]
for n in N:
  dx=(math.pi/2)/n
     
  x=numpy.linspace(0,math.pi/2,n)
  x_Odd=x[1::2]
  x_Even=x[2:n-1:2]
  
  y=numpy.cos(x)
  y_Odd=numpy.cos(x_Odd)
 
  Sum_Odd=y_Odd.sum()
 
  
  y_Even=numpy.cos(x_Even)
  Sum_Even=y_Even.sum()
  
  integral=2*((1./6)*y[0]+(2./3)*Sum_Odd+(1./3)*Sum_Even+(1./6)*y[-1])*dx
  err=numpy.absolute(1-integral)
  
  print"The Integral= "+repr(integral)+" with error "+repr(err)