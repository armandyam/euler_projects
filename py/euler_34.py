#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ajay Rangarajan, Jeyashree Krishnan"
__email__ = "rangarajan, krishnan@aices.rwth-aachen.de"


import numpy as np
import math as mp
import matplotlib.pyplot as plt

fc = []
n_val = []

def factdigits(n):
	string = str(n)
	ans = 0
	for val in string:
		ans = ans + mp.factorial(int(val))
	fc.append(ans)
	n_val.append(n)
	if(ans == n):
		return ans
	else:
		return 0

fin_pow = 8
result = 0
for i in range(10, 10**fin_pow):
	result = result + factdigits(i)
	if(factdigits(i)):
		print i

print result

plt.plot(n_val, fc, 'b*')
plt.plot(n_val, n_val)
plt.show()

"""
http://www.mathblog.dk/project-euler-34-factorial-digits/
https://projecteuler.net/problem=34
"""