import matplotlib.pyplot as plt
import numpy as np

max_no = -1
i_max = 0
j_max = 0
for i in range(100,1000):
	for j in range(100, 1000):
		number = i*j
		rev_number = str(number)[::-1]
		if(str(number)==rev_number):
			if(number>max_no):
				max_no = number
				i_max = i
				j_max = j

print max_no, i_max, j_max
'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''
