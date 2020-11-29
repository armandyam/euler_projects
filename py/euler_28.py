
#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ajay Rangarajan, Jeyashree Krishnan"
__email__ = "rangarajan, krishnan@aices.rwth-aachen.de"


import numpy as np 

def diag(n):
	if(n==1):
		UR = 1
		UL = 0
		LL = 0
		LR = 0
	else:
		[old_ur, old_ul, old_ll, old_lr] = diag(n-2)
		UR = old_ur + n*2 + (n-2)*2
		UL = UR - (n-1)
		LL = UR - 2*(n-1)
		LR = UR - 3*(n-1)
	return UR, UL, LL, LR
sz = 3
sum_diag = 0
for i in range(0, (sz+1)/2):
	n = 2*i + 1
	[ur, ul, ll, lr] = diag(n)
	sum_diag = sum_diag + ur + ul + ll + lr
print sum_diag
"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

We can also notice that all the numbers are odd and are with a few numbers skipped between them. SO the general
equation for any number is D = 1 + k*(n-1) where k = 0,1,2,3 and n = 1,3,5,7.... So summing over n for each k
gives us the total
"""