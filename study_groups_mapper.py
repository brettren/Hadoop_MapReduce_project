#!/usr/bin/python

# Writing a mapreduce program that for each forum thread 
# (that is a question node with all it's answers and comments) 
# would give us a list of students that have posted there - either asked the question, 
# answered a question or added a comment. If a student posted to that thread several times,
# they should be added to that list several times as well(repeated), 
# to indicate intensity of communication.


# Mapper

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader, None)

for line in reader:
	if len(line) == 19:
		node_id = line[0]
		author_id = line[3]
		node_type = line[5]
		abs_parent_id = line[7]
		if node_type == "question":
			print "{0}\t{1}".format(node_id, author_id)
		else:
			# for "answer" and "comments", output the top parent, which is the question id
			print "{0}\t{1}".format(abs_parent_id, author_id)

