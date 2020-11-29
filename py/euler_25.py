#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ajay Rangarajan, Jeyashree Krishnan"
__email__ = "rangarajan, krishnan@aices.rwth-aachen.de"


import matplotlib.pyplot as plt
import numpy as np
import time

start = time.clock()
res = 0
n = 3
while(res<1000):
	fnm1 = 1
	fnm2 = 1
	for i in range(0,n):
		fn = fnm1 + fnm2
		fnm2 = fnm1
		fnm1 = fn

	res = len(str(fn))

	n = n + 1

print res, n+2, fn
end = time.clock()

print end-start

"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""