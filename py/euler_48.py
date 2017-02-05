import numpy as np 

ans = 0
for i in range(1, 1001):
	ans = ans + i**i
print str(ans)[-10:]