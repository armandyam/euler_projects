#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ajay Rangarajan, Jeyashree Krishnan"
__email__ = "rangarajan, krishnan@aices.rwth-aachen.de"


import numpy as np 
def is_prime(number):
	# If the number is 0 or 1 then it is not a prime number
	if(number==1 or number==0):
		return False
	# If the number is 2 then it has to explicitly return 0
	elif(number == 2):
		return True
	else:
	# Check upto the square root of the number
		limit = np.int(np.ceil(np.sqrt(number)))+1
		tf = []
		# Check if any of divisors exist if they do then return False else return True
		for i in range(2, limit):
			if(number%i==0):
				tf.append(False)
			else:
				tf.append(True)
	ans = True
	for i in range(0, len(tf)):
		ans = ans and tf[i]
	return ans

# Calculate smallest factors of a number
def factors(number):
	for i in range(2, number+1):
		if(number%i==0):
			return i

# Calculate all the prime factors
def prime_factors(n):
	factor = []
	while (n != 1):
		p = factors(n)
		n = n/p
		factor.append(p)
	return factor
