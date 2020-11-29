#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ajay Rangarajan, Jeyashree Krishnan"
__email__ = "rangarajan, krishnan@aices.rwth-aachen.de"


import matplotlib.pyplot as plt
import numpy as np

number = 4
start = 2
no_comp = 0
no_prime = 0
prime_arr = [2,3]
end = 9999

while(no_prime<end):
	lim = np.int(np.ceil(np.sqrt(number)))+1
	for i in range(start, lim):
		if(number%i==0):
			no_comp +=1
			number +=1
			start = 2
			break
		if(i==lim-1):
			prime_arr.append(number)
			no_prime+=1
			number +=1
			start = 2
print prime_arr[-1]
'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''
