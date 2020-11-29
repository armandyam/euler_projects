#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ajay Rangarajan, Jeyashree Krishnan"
__email__ = "rangarajan, krishnan@aices.rwth-aachen.de"


import numpy as np
import math as mp
import matplotlib.pyplot as plt
from decimal import *
import itertools
import isprime as isp


## find if a given number is pandigital
def is_pandigital(n):
	sort = "".join(sorted(str(n)))
	if (sort == '123456789'):
		return n
	else:
		return 0

#the max p can be only 4 digits and should be < 9876
maxval = 9999+1

#search for all pandigital numbers less than maxval
#where p*2 has same number of digits as p
#n2 is the case where p*2 has 1 digit more than p

for k in range(1, maxval):
	p = str(k)
	n1 = int(np.ceil(9./len(p)))
	n2 = int(np.floor((9. - len(p))/(len(p)+1)+1))
	for i in range(n2, n1+1):
		pan = ''
		for j in range(1, i+1):
			val = int(p)*j
			pan = pan + str(val)
		if (is_pandigital(int(pan))):
			print p, pan

'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

# p, n
# p * 1
# p * 2
# ...
# len(p) + len(p) + len(p) ..n  times =  n*len(p) = a
# len(p) + len(p)+1 + len(p)+1 ..n  times = (n-1)*(len(p)+1)+len(p) = b
# a <= 9
# b <= 9