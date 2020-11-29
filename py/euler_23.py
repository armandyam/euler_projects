#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ajay Rangarajan, Jeyashree Krishnan"
__email__ = "rangarajan, krishnan@aices.rwth-aachen.de"


import numpy as np
import math as math
from decimal import *
# import euler_23_import as imp
# import matplotlib.pyplot as plt

def d(n):
	sum = 0
	for i in range(1, n/2+1):
		if(n%i==0):
			sum = sum + i	
	return sum

count = 0
ans = 0
temp = 0
sum1 = 0
for n in range(24, 28124):
	for i in range(11, n/2+1):
		p1 = d(i)
		p2 = d(n-i)
		if(p1>i and p2>(n-i)):
			if(temp != n):
				sum1 = sum1+n
				temp = n

print sum1
"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""