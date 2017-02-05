import numpy as np 
import isprime as isp

def prime_factors(number):
	fac = []
	limit = np.int(np.ceil(np.sqrt(number)))
	for i in range(2, limit):
		# print i
		if (number%i ==0 and isp.is_prime(i)):
			print i
			fac.append(i)
	return fac

print prime_factors(300)
# print isp.is_prime(2)