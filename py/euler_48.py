#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ajay Rangarajan, Jeyashree Krishnan"
__email__ = "rangarajan, krishnan@aices.rwth-aachen.de"

import numpy as np 

ans = 0
for i in range(1, 1001):
	ans = ans + i**i
print str(ans)[-10:]