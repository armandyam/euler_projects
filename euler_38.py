import numpy as np
import math as mp
import matplotlib.pyplot as plt
from decimal import *
import itertools
import isprime as isp

def is_pandigital(n):
	sort = "".join(sorted(str(n)))
	if (sort == '123456789'):
		return n
	else:
		return 0

maxval = 193 #987654322

for k in range(1, maxval/2):
	p = str(k)
	n1 = int(np.ceil(9./len(p)))
	n2 = int(np.floor((9. - len(p))/(len(p)+1)+1))
	for i in range(n2, n1+1):
		pan = ''
		for j in range(1, i+1):
			val = int(p)*j
			pan = pan + str(val)
		print is_pandigital(int(pan)), p
	# print p



# p, n
# p * 1
# p * 2
# ...
# len(p) + len(p) + len(p) ..n  times =  n*len(p) = a
#  len(p) + len(p)+1 + len(p)+1 ..n  times = (n-1)*(len(p)+1)+len(p) = b
# a <= 9
# b <= 9