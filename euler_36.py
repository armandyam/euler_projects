import numpy as np
import math as mp
import matplotlib.pyplot as plt
from decimal import *
import itertools
import isprime as isp

def is_palindrome(number):
	rev_number = str(number)[::-1]
	if(str(number)==rev_number):
		return True
	else:
		return False

ans = 0
for i in range(1,1000000):
	base_10 = i
	base_2 = int("{0:b}".format(i))
	if is_palindrome(base_10) and is_palindrome(base_2):
		ans = ans + base_10

print ans