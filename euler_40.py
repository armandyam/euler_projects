import numpy as np 

# number of one digit numbers = 9
# number of two digit numbers = 90
# number of three digit numbers = 900
# number of p digit number numbers = 9 followd by p-1 zeros

# nth position 9*one digit+90*two digits+900*three digits and so on
def position_p(n):
	val = 0
	digit = 1
	power = 0
	while(val<n):
		k = 10**power
		val = digit*9*k + val
		power += 1
		digit += 1
	
	k = 10**(power-1)
	digit = digit - 1
	val = val - digit*9*k
	# print n-val, digit
	diff_pos = n-val
	last  = np.floor(diff_pos/digit)# last number of digit numbered numbers
	# numers have to be 10**digit,10**digit+1,...,10*digit+(last)
	string_digit = ''
	for i in range(0, int(last)+1):
		string_digit = string_digit + str(10**(digit-1)+i)
	return int(string_digit[diff_pos-1])

ans = position_p(1) * position_p(10) * position_p(100) * position_p(1000) * position_p(10000) * position_p(100000) * position_p(1000000)
print ans
