import numpy as np
import math as mp
import matplotlib.pyplot as plt
from decimal import *
import itertools
import isprime as isp
from collections import deque


def longestWord(letters):
	val = deque(letters)
	out = []
	for i in range(0, len(val)):
		p = list(val)
		val.rotate(1)
		string = ''
		for j in p:
			string = string+j
		out.append(string)
	return out
	
def digit(n):
	digit_str = []
	string = str(n)
	for val in string:
		digit_str.append(val)
	return digit_str

count  = 0
for n in range(1,1000001):
	str_digit = digit(n)
	nums = longestWord(str_digit)
	tf = True
	for i in range(0, len(nums)):
		tf = isp.is_prime(int(nums[i])) and tf

	if(tf==True):
		count = count + 1
		print nums, ' is circular prime'
print count
	# a = list(itertools.permutations(str_digit, len(str_digit)))
	# for i in range(0, len(a)):
		# print a[1][1]
