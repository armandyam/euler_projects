#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ajay Rangarajan, Jeyashree Krishnan"
__email__ = "rangarajan, krishnan@aices.rwth-aachen.de"


import numpy as np 

def sorted_num(num):
	sort = []
	for i in range(1, 7):
		sort.append(int("".join(sorted(str(i*num)))))
	return sort
def checkEqual(lst):
   return lst[1:] == lst[:-1]

found = False
num = 10
while(found == False):
	x = sorted_num(num)
	if(checkEqual(x)):
		found = True
	else:
		num = num + 1
print num