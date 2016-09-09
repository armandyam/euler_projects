import matplotlib.pyplot as plt
import numpy as np

l_prime = 0
number = 13714
limit = np.int(np.ceil(np.sqrt(number)))

a = []

for i in range(1, limit):
	if(number%i==0):
		number = number/i
		limit = np.int(np.ceil(np.sqrt(number)))
		a.append(number)

print a[len(a)-2]
'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''