import numpy as np
import isprime as isp

k = 1
square = True
while(square==True):
	odd_no = 2*k+1
	if (isp.is_prime(odd_no)==False):
	# odd_no is composite
		r = (odd_no-1)/2
		tf = False
		for i in range(1,r):
			prime = 2*i+1
			if(isp.is_prime(prime)):
				# calculate difference between the odd number and any prime number less that itself
				diff = odd_no-prime
				sq_no = np.sqrt(diff/2.0)
				if(np.floor(sq_no) != sq_no):
					tf = (np.floor(sq_no) != sq_no) or tf
		if(tf == True):
			k += 1
		else:
			square = False
	else:
		k+=1
	print odd_no
print odd_no