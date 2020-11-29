#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ajay Rangarajan, Jeyashree Krishnan"
__email__ = "rangarajan, krishnan@aices.rwth-aachen.de"


import numpy as np

prod = 1.0
for a in range(1, 10):
	for b in range(1, 10):
		for c in range(1, 10):
			if(a!=b and b!=c):
				lhs = 9*a*c
				rhs = b*(10*a-c)
				if(lhs==rhs):
					prod = prod * float(a)/float(c)
print prod*100
# for a in range(1, 10):
# 	for b in range(1, 10):
# 		for c in range(1, 10):
# 			if(a!=b and b!=c):
# 				lhs = 9*b*c
# 				rhs = a*(10*c-b)
# 				if(lhs==rhs):
# 					print "Eq2 ",10*a+b,"/",10*c+a
# 					
"""
https://projecteuler.net/problem=33
"""