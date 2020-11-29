#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ajay Rangarajan, Jeyashree Krishnan"
__email__ = "rangarajan, krishnan@aices.rwth-aachen.de"


import matplotlib.pyplot as plt
import numpy as np

def is_composite(number):
	limit = np.int(np.ceil(np.sqrt(number)))+1
	a = 0
	for i in range(2, limit):
		if(number%i==0):	
			return 0
		if(i==limit-1):
			return number

ans = 2000000
sum_comp = 5
for i in range(4, ans+1):
	sum_comp += is_composite(i)
print sum_comp
'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''