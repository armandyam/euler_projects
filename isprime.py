import numpy as np 
def is_prime(number):
	if(number==1 or number==0):
		return False
	else:
		limit = np.int(np.ceil(np.sqrt(number)))+1
		for i in range(2, limit):
			if(number%i==0):	
				return False
			elif(i==limit-1):
				return True