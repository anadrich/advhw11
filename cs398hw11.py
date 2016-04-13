# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 00:30:01 2016

@author: anadrich
"""

csv_raw = "1,2,3"


import csv
data = list(csv.reader(open('q2.csv')))
data

arr=[1,2,3,4,5,6,7,42,42]
odd_nums = [x for x in arr if x % 2 == 1]

courses = dict([('eecs 445','machine learning'),('eecs 484','databases'),('stats 425','probability')])

def print_courses(courses):
    for x in courses:
        print x + ": " + courses[x]
        
def print_courses_new(courses,courses2):
    myDict = dict()
    readList = list(csv.reader(open(courses)))
    for i in range(1,len(readList)):
        myDict[readList[i][0]] = readList[i][1]
    newDict = myDict.copy()
    newDict.update(courses2)
    print_courses(newDict)
  

from sh import ls
from sh import git


dir = ls("/")
for elt in dir:
    if git("status")!="fatal: Not a git repository (or any of the parent directories): .git"
        git("pull")