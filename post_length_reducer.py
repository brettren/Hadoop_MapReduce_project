#!/usr/bin/python

# Reducer

# recording the post length, num of answers, and total answer length

import sys

oldKey = None
totalAnswerLength = 0
postLength = 0
numAnswers = 0

print "Question Node ID |", "\t", "Question Length |", "\t", "Average Answer Length" 

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 3:
		continue

	thisKey, node_type, len_body = data_mapped

	if oldKey and oldKey != thisKey:
		if numAnswers != 0:
			print oldKey, "\t", postLength, "\t", totalAnswerLength / numAnswers
		else:
			print oldKey, "\t", postLength, "\t", 0
		oldKey = thisKey
		totalAnswerLength = 0
		postLength = 0
		numAnswers = 0

	oldKey = thisKey
	if node_type == "question":
		postLength = int(len_body)
	elif node_type == "answer":
		totalAnswerLength += float(len_body)
		numAnswers += 1

if oldKey != None:
	if numAnswers != 0:
		print oldKey, "\t", postLength, "\t", totalAnswerLength / numAnswers
	else:
		print oldKey, "\t", postLength, "\t", 0