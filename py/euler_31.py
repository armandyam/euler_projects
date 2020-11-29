#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ajay Rangarajan, Jeyashree Krishnan"
__email__ = "rangarajan, krishnan@aices.rwth-aachen.de"


import numpy as np

tot = 200
e1 = tot/1+1
e2 = tot/2+1
e3 = tot/5+1
e4 = tot/10+1
e5 = tot/50+1
e6 = tot/100+1
e7 = tot/200+1
count = 0
for k7 in range(0, e7):
	for k6 in range(0, e6):
		for k5 in range(0, e5):
			for k4 in range(0, e4):
				for k3 in range(0, e3):
					for k2 in range(0, e2):
						for k1 in range(0, e1):
							val = k1*1 + k2*2 + k3*5 + k4*10 + k5*50 + k6*100 + k7*200
							if(val == tot):
								count = count+1
print count
"""
https://projecteuler.net/problem=32
"""