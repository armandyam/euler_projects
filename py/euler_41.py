#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ajay Rangarajan, Jeyashree Krishnan"
__email__ = "rangarajan, krishnan@aices.rwth-aachen.de"


import numpy as np 
import isprime as isp

## find if a given number is pandigital
def is_pandigital(n):
	d = len(str(n))
	sort = "".join(sorted(str(n)))
	if(d>9):
		print 'error'
		return 0
	else:
		val = ''
		for i in range(1, d+1):
			val = val+str(i)
		if (sort == val):
			return n
		else:
			return 0

maxval = 90000000
for i in np.arange(maxval, 0, -1):
	# print 'Entered here!'
	if(is_pandigital(i)):
		if(isp.is_prime(i)):
			print i
			break