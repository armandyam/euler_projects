import numpy as np
import math

def is_palindrome(number):
	rev_number = str(number)[::-1]
	if(str(number)==rev_number):
		return True
	else:
		return False

def find_sum(num):
	rev_number = str(num)[::-1]
	ans = num + int(rev_number)
	return ans

maxnum = 10000
count = 0

for i in range(1, maxnum):
	num = i
	for j in range(0, 50):
		if(is_palindrome(num)==False):
			num = find_sum(num)
		else:
			count = count + 1
			print i
			break

print maxnum-count