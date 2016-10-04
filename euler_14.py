import numpy as np


'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
'''

def oddoreven(n):
	if (n%2 ==0):
		return n/2
	elif (n ==1):
		return 0
	else:
		return 3*n+1

max = 1000000

x = -1
val = 0

for i in range(2,max):
	n = i
	k=0
	while (n != 0):
		# print n
		p = oddoreven(n)
		n =p
		k += 1
	if (k > x):
		x = k
		val = i

print x, val

#525 837799

