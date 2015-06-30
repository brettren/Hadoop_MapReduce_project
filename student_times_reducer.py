#!/usr/bin/python

# Reducer

import sys

oldKey = None

hours = {}

print "Student ID |", "\t", "Hour"

for i in range(24):
	# occurance in each hour
	hours[i] = 0

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue

	thisKey, thisValue = data_mapped

	if oldKey and oldKey != thisKey:
		highest = max(hours.values())
		for k,v in hours.items():
			if v == highest:
				print oldKey, "\t", k
		oldKey = thisKey
		for i in range(24):
			hours[i] = 0

	oldKey = thisKey
	hours[int(thisValue)] += 1

if oldKey != None:
	highest = max(hours.values())
	for k,v in hours.items():
		if v == highest:
			print oldKey, "\t", k