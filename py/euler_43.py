#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ajay Rangarajan, Jeyashree Krishnan"
__email__ = "rangarajan, krishnan@aices.rwth-aachen.de"


import numpy as np
import math as math
from decimal import *
import itertools


# check sub-string divisibility

def if_sub_string_div(number):
	# converting number to string to extract the digits
	# Concatenating three digits at a time
	d1 = int(number[1]+number[2]+number[3])
	d2 = int(number[2]+number[3]+number[4])
	d3 = int(number[3]+number[4]+number[5])
	d4 = int(number[4]+number[5]+number[6])
	d5 = int(number[5]+number[6]+number[7])
	d6 = int(number[6]+number[7]+number[8])
	d7 = int(number[7]+number[8]+number[9])
	# Check for divisibility with the first 7 prime numbers
	if(d1%2==0 and d2%3==0 and d3%5==0 and d4%7==0 and d5%11==0 and d6%13==0 and d7%17==0):
		return int(number)
	else:
		return 0


dig = 10
# Generating all permutations of 10 digit numbers
all_pan = list(itertools.permutations(range(dig), dig))
sum_ans = 0
for item in all_pan:
	# Converting each tuple into a string
	number = ''
	for dig in item:
		number += str(dig)
	# Retain the number as a string so as not to lost the leading zero
	if(if_sub_string_div((number))):
		sum_ans += if_sub_string_div((number))
print sum_ans


