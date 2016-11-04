import numpy as np
import math as math
from decimal import *
# import matplotlib.pyplot as plt

def d(n):
	sum = 0
	for i in range(1, n/2+1):
		if(n%i==0):
			sum = sum + i	
	return sum
ab = []

for number in range(1, 28124):
	if (d(number)>number):
		ab.append(number)