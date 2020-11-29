#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ajay Rangarajan, Jeyashree Krishnan"
__email__ = "rangarajan, krishnan@aices.rwth-aachen.de"



import numpy as np 

p = np.arange(0,1001,2)

maxcount = 0
pmax = 0

# three conditions: p is even; a+b+c= p; a^2+b^2=c^2
# b = p * (a - p/2) / (a - p)
for i in p:
	count = 0
	for a in range(1, i-1):
		b = i*(a-i/2.)/(a-i)
		if (b.is_integer() and b>0):
			count +=1
	if(count> maxcount):
		maxcount = count
		pmax = i			

print pmax, maxcount

'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''9