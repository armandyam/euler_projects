#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ajay Rangarajan, Jeyashree Krishnan"
__email__ = "rangarajan, krishnan@aices.rwth-aachen.de"


import numpy as np
import math


def digit_sum(number):
	return sum(int(digit) for digit in str(number))

maxsum = -1
for a in range(0, 100):
	for b in range(0, 100):
		num = a**b
		val = digit_sum(num)
		if(val>maxsum):
			maxsum = val
print maxsum