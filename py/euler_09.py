import matplotlib.pyplot as plt
import numpy as np

for i in range(1,500):
	c = i
	for j in range(1, i):
		b = j
		a = np.sqrt(i**2 - j**2)
		if(a+b+c==1000):
			print a, b, c
			print a*b*c
'''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''