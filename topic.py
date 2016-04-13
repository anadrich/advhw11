# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 03:33:02 2016

@author: anadrich
"""

import sys 
import re 

#word = sys.argv[1]
#number = sys.argv[2]

files = []

class Searcher():
	def search(self,word,number,files):
		finalList = []
		for filename in files:
			with open(filename) as openfile:
				filestr = ""
				for line in openfile:
					filestr+=line
				if filestr.count(word)>=int(number):
					finalList.append(filename)
		return finalList




