#!/usr/bin/python

import datetime,os,glob

from datetime import date

filePath = "C:\Users\snune\log"

maxDaystoKeep= 0  

currentdate=date.today() # Stores current date

ListFiles = glob.glob(filePath + '\*.txt')
print ListFiles
#os.listdir(filePath) # List the files in that directory
