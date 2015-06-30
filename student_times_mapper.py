#!/usr/bin/python

# In this exercise your task is to find for each student what is the hour during 
# which the student has posted the most posts. Output from reducers should be:

# author_id    hour

import sys
import csv

# Mapper

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader, None)

for line in reader:
	if len(line) == 19:
		author_id = line[3]
		hour = int(line[8][11:13])
		print "{0}\t{1}".format(author_id, hour)

