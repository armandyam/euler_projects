#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ajay Rangarajan, Jeyashree Krishnan"
__email__ = "rangarajan, krishnan@aices.rwth-aachen.de"


import numpy as np

def panidentity(n):
	string = str(n)
	if(len(string)>5):
		for i in string:
			if(i!=0):
				return True
			else:
				return False
	else:
		return True
count = 0


def check(prod, i, j):
	x = [i,j,prod]
	b = int(''.join(map(str, x)))
	sort = "".join(sorted(str(b)))
	if (sort == '123456789'):
		return prod
	else:
		return 0


a1 = range(1, 10)
a2 = range(10, 100)
a3 = range(100, 1000)
a4 = range(1000, 10000)


ans = []

for i in a1:
	for j in a3:
		prod = i*j
		if(panidentity(prod)):
			if(check(prod, i, j)):
				ans.append(check(prod,i,j))
				count += 1
				print i, j, prod
		else:
			ans = ans
	for j in a4:
		prod = i*j
		if(panidentity(prod)):
			if(check(prod, i, j)):
				ans.append(check(prod,i,j))
				count += 1
				print i, j, prod
		else:
			ans = ans


for i in a2:
	for j in a3:
		prod = i*j
		if(panidentity(prod)):
			if(check(prod, i, j)):
				ans.append(check(prod,i,j))
				count += 1
				print i, j, prod
		else:
			ans = ans
	for j in a4:
		prod = i*j
		if(panidentity(prod)):
			if(check(prod, i, j)):
				ans.append(check(prod,i,j))
				count += 1
				print i, j, prod
		else:
			ans = ans

print list(set(ans))
print 'number, sum of those weird numbers=', count,  sum(list(set(ans)))
"""
https://projecteuler.net/problem=32
"""