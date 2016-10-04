import matplotlib.pyplot as plt
import numpy as np

def no_divisor(n):
	count_loc = 0
	for i in range(2, int(np.ceil(n/2))+1):
		if(n%i==0):
			count_loc = count_loc + 1
	return count_loc

count = 0
ite = 1
no = []
div = []
while(count<=400):
	number = ite*(ite+1)*0.5
	count = no_divisor(number) + 2
#	print number, count
	no.append(int(number))
	div.append(count)
	ite = ite+1
print int(number)
plt.plot(no, div, 'o--')
plt.grid(True)
plt.savefig('euler_12.pdf')
#plt.show()