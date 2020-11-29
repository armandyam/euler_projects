#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ajay Rangarajan, Jeyashree Krishnan"
__email__ = "rangarajan, krishnan@aices.rwth-aachen.de"


import numpy as np
import math as math
from decimal import *

with open('names.txt', 'r') as myfile:
    data=myfile.read().replace('"', '')

text = data
text = data.split(',')
# print text


text= sorted(text)

def find_value(input):
	# print input
	input = input.lower()
	# print input
	output = []
	for character in input:
	    number = ord(character) - 96
	    output.append(number)
	return sum(output)

# print find_value("colin")
# 

sum1 = 0

for id, name in enumerate(text):
	sum1 = sum1 +(id+1)* find_value(name) 

print sum1

# print find_value('AB')
"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""