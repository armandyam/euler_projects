import numpy as np
import isprime as isp


## find if a number is a perfect square
def is_perfect_sqaure(n):
	if(np.floor(n) == n):
		return True
	else:
		return False


# initialize counter for non-convergence of Goldbach's Conjecture
k = 1
search = True
while(search == True):
	# initialize starting odd number
	odd_no = 2*k+1

	# Check if the generated odd number is composite. If not increment 'k'
	if (isp.is_prime(odd_no)==False):
		# 'odd_no' is composite
		tf = []
		# Generate all odd numbers below the given odd composite number
		for i in range(1,k):
			prime = 2*i+1
			# selected_prime = 0
			# selected_square = 0
			# Check if these odd numbers are prime
			if(isp.is_prime(prime)):
				# calculate difference between the odd number and any prime number less that itself
				diff = odd_no-prime
				sq_no = np.sqrt(diff/2.0)
				tf.append(is_perfect_sqaure(sq_no))
				if(is_perfect_sqaure(sq_no)):
					selected_prime = prime # Select the number for which we have a solution to Goldbach's conjectures
					selected_square = sq_no
		ans = False
		for i in tf:
			if i==True:
				ans = True
		if(ans==True):# This number satisfies Goldbach's conjection
			k += 1
			print odd_no, '=', selected_prime, '+', '2 x',int(selected_square),'^2' # Showing the case for which the Conjecture is satisfied
		else:
			print 'Found the execption. It is: ', odd_no
			search = False
	else:
		k+=1