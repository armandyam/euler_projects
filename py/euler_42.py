#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ajay Rangarajan, Jeyashree Krishnan"
__email__ = "rangarajan, krishnan@aices.rwth-aachen.de"


import numpy as np


# calculate the word value

def calc_score(input):
	input = input.lower()
	output = []
	for character in input:
	    number = ord(character) - 96
	    output.append(number)
	return sum(output)

def check_triangle_number(d):
	# d = 0.5*n*(n+1)
	# the equation is n^2+n-2*d = 0, a = 1, b = 1, c=-2*d in ax^2+bx+c=0
	a = 1
	b = 1
	c = -2*d
	disc = b**2-4*a*c
	# discriminant has to be greater than 0
	if disc<0:
		return 0
	else:
		# check if n is an integer and n is positive
		sol_1 = (-b + np.sqrt(disc))/(2*a)
		sol_2 = (-b - np.sqrt(disc))/(2*a)
		# solution or solutions have to be positive
		if (sol_1>0) or (sol_2>0):
			if (sol_1>0) and (sol_2 > 0):
				# solution has to be an integer
				if (np.floor(sol_1)==sol_1 and np.floor(sol_2)==sol_2 and (sol_1 == sol_2)):
					return sol_1
			elif (sol_1 > 0 and np.floor(sol_1)==sol_1):
				return sol_1
			elif (sol_2 > 0 and np.floor(sol_2)==sol_2):
				return sol_2	
			else:
				return 0		
		else:
			return 0

# read file string by string

with open('words.txt', 'r') as myfile:
    data=myfile.read().replace('"', '')

text = data
text = data.split(',')

count = 0
for word in text:
	d = calc_score(word)
	if (check_triangle_number(d)):
		count +=1

# number of triangle words
print count