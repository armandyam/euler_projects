#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ajay Rangarajan, Jeyashree Krishnan"
__email__ = "rangarajan, krishnan@aices.rwth-aachen.de"


import numpy as np
import math as mp
import matplotlib.pyplot as plt
from decimal import *
import itertools
import isprime as isp

def is_sub_prime(n):
	tf = True
	for i in range(1, len(str(n))):
		n_sub =  int(str(n)[:-i])
		tf = isp.is_prime(n_sub) and tf
	if(tf):
		tf2 = True
		for j in range(1, len(str(n))):
			tf2 = isp.is_prime(int(str(n)[j:])) and tf2
	if(tf and tf2):
		return n
	else:
		return 0

k = 0
n = 10
ans = 0
while(k<12):
	if(isp.is_prime(n)):
		if(is_sub_prime(n)):
			k = k+1
			print is_sub_prime(n)
		ans = ans + is_sub_prime(n)
	n = n + 1
print ans

