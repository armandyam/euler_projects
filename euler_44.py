import numpy as np 

def penty(n):
	p_n = n * (3*n-1)/ 2
	return p_n

def pent_sum(rhs):
	# rhs = n*(3n-1)
	# the equation is n^2+n-rhs = 0, a = 3, b = -1, c=-rhs in ax^2+bx+c=0
	a = 3
	b = -1
	c = -rhs
	disc = b**2-4*a*c
	# discriminant has to be greater than 0
	if disc<0:
		return 0
	else:
		# check if n is an integer and n is positive
		sol_1 = (-b + np.sqrt(disc))/(2*a)
		sol_2 = (-b - np.sqrt(disc))/(2*a)
		# solution or solutions have to be positive
		if (sol_1>0) or (sol_2>0):
			if (sol_1>0) and (sol_2 > 0):
				# solution has to be an integer
				if (np.floor(sol_1)==sol_1 and np.floor(sol_2)==sol_2 and (sol_1 == sol_2)):
					return sol_1
			elif (sol_1 > 0 and np.floor(sol_1)==sol_1):
				return sol_1
			elif (sol_2 > 0 and np.floor(sol_2)==sol_2):
				return sol_2	
			else:
				return 0		
		else:
			return 0


max = 1000000

for n in range(max):
	for m in range(max):
		rhs = penty(n)+ penty(m)
		if (pent_sum(rhs) != 0):
			x = pent_sum(rhs)
			rhs_new = penty(n)- penty(m)
			if(pent_sum(rhs_new) != 0):
				y = pent_sum(rhs_new)
				print x, y


