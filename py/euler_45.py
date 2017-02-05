import numpy as np

def tri(n):
	return n*(n+1)/2

# def penty(m):
# 	return m * (3*m-1)/ 2

# def hex(k):
# 	return k*(2*k-1)

def pent_sol(rhs):
	# rhs = n*(3n-1)/2
	# the equation is 3n^2-n-2*rhs = 0, a = 3, b = -1, c=-2*rhs in ax^2+bx+c=0
	a = 3
	b = -1
	c = -2*rhs
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

def hex_sol(rhs):
	# rhs = n*(2n-1)
	# the equation is 2n^2-n-rhs = 0, a = 2, b = -1, c=-rhs in ax^2+bx+c=0
	a = 2
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

n = 286
integers = False
while(integers==False):
	rhs = tri(n)
	m = pent_sol(rhs)
	k = hex_sol(rhs)
	integers = m and k
	n+=1
print tri(n-1), m, k
