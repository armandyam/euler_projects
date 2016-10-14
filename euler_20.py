import numpy as np
import math as math
from decimal import *

number =  math.factorial(100)
a = sum(int(digit) for digit in str(number))
getcontext().prec = 30
print a, np.pi

a = (1./3.)

print type(a)