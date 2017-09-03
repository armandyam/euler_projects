import numpy as np
import math
from fractions import Fraction

a = []
b = []
x_a = []
x_b = []
count = 0
a.append(2)
b.append(1)
for i in range(0, 1001):
	nume_temp = 2*a[i]+b[i]
	deno_temp = a[i]
	a.append(nume_temp)
	b.append(deno_temp)
	x_a.append(a[i]+b[i])
	x_b.append(a[i])
	nume_len = len(str(x_a[i]))
	deno_len = len(str(x_b[i]))
	if(nume_len>deno_len):
		count = count + 1
print count

# Y_{N} = 2 + 1/Y_{N-1}
# Y_{1} = 2/1
# To preserve the fractions we save Y_{i} = a_{i}/b_{i}
# a_{i+1} = 2*a_{i} + b_{i}
# b_{i+1} = a_{i}
# The final fraction is X_{i} = 1 + 1/Y_{i}
# Which means X_{i} = 1 + 1/(a_{i}/b_{i}) = (a_{i}+b_{i})/a_{i}