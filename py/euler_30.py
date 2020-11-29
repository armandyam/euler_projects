#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ajay Rangarajan, Jeyashree Krishnan"
__email__ = "rangarajan, krishnan@aices.rwth-aachen.de"


import numpy as np 

def fifth_power(n):
	string = str(n)
	val = 0
	for i in string:
		val = val + int(i)**5
	return val

sum1 = 0 

for i in range(2,9999999):
	x = fifth_power(i)
	if (x==i):
		sum1 = sum1 + i
		print i

print sum1

"""
https://projecteuler.net/problem=30
"""