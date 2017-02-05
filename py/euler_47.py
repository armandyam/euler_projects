import numpy as np 
import isprime as isp

n = 4
start = 2


found = True

while(found==True):
	consecutive = []
	factors = []
	for i in range(0, n):
		consecutive.append(start+i)
		# Consecutive stores n consevutive natural numbers
		repeated_prime_factors = isp.prime_factors(consecutive[i])
		# Prime_factors calculates all the prime factors of consevutive[i] with repitition
		unique_fractors = np.unique(repeated_prime_factors)
		# unique calculates the unique number of prime factors of consecutive[i]
		length_unique_factors = len(unique_fractors)
		# factors stores the number of unique factors of consecutive[i]
		factors.append(length_unique_factors)
	tf = []
	for i in factors:
		if(i!=n):
			tf.append(0)
		else:
			tf.append(1)
	# print start, factors
	if(sum(tf)==len(tf)):
		print 'Solution found: ', consecutive
		found=False
	else:
		print start
		start+=1

