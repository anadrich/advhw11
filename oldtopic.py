# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 03:33:02 2016

@author: anadrich
"""

import sys 
import re 

word = sys.argv[1]
number = sys.argv[2]

files = []

for i in range(3,len(sys.argv)):
	with open(sys.argv[i]) as openfile:
		filestr = ""
		for line in openfile:
			filestr+=line
		if filestr.count(word)>=int(number):
			print sys.argv[i]


