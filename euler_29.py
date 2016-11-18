import numpy as np 

begin = 2
end = 101
val = []
for i in range(begin,end):
	for j in range(begin, end):
		a = i
		b = j
		val.append(a**b)
val_s = sorted(list(set(val)))
print len(val_s)

'''
https://projecteuler.net/problem=29
'''