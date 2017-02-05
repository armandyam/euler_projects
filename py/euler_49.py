from itertools import permutations
import numpy as np 
import isprime as isp



for i in range(1000, 10000):
	if(isp.is_prime(i)):
		perms = [''.join(p) for p in permutations(str(i))]
		count = 0
		permutations_prime = []
		for j in set(perms):
			n = int(j)
			if(isp.is_prime(n)):
				permutations_prime.append(j)
				count += 1
		if(count>2):
			print permutations_prime