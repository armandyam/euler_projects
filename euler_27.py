import numpy as np 
import isprime as isp

max_a = 0
max_b = 0
max_n = 0
for a in range(-999,1000):
	for b in range(-1001,1001):
		n=0
		p = 5
		while ((p>0) and isp.is_prime(p)==True):
			n = n + 1
			p = n**2 + a*n + b
		if(n>max_n):
			max_n = n
			max_a = a
			max_b = b
print max_a * max_b