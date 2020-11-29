#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ajay Rangarajan, Jeyashree Krishnan"
__email__ = "rangarajan, krishnan@aices.rwth-aachen.de"


from itertools import permutations
import numpy as np 
from isprime import *

prime = []
maxprime = 1000000
winlen = []   
num = []

for i in range(1, maxprime):
	if(is_prime(i)):
		prime.append(i)

window = np.arange(2,len(prime)-1,1)
counter = 0
for pos in window:
	for i in range(0, len(prime)-pos):
		current_sum = sum(prime[i:i+pos])
		if(is_prime(current_sum) and current_sum < maxprime):
			winlen.append(pos)
			num.append(current_sum)
			counter = counter + 1
			print counter

ans = num[np.argmax(winlen)]
print ans

"""The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?"""