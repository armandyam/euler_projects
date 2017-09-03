import numpy as np
import math

def nCr(n, r):
	return math.factorial(n)/(math.factorial(n-r)*math.factorial(r))

maxval = 1000000
count = 0
for i in range(23, 101):
	for j in range(0, i):
		if(nCr(i,j)>maxval):
			count = count + 1
print count
