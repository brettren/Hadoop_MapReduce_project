#!/usr/bin/python

# Write a mapreduce program that would output Top 10 tags, 
# ordered by the number of questions they appear in.

# only look at tags appearing in questions themselves

# Mapper

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader, None)

for line in reader:
	if len(line) == 19:
		node_id = line[0]
		node_type = line[5]
		tagnames = line[2]
		if node_type == "question":
			print "{0}\t{1}".format(node_id, tagnames)
