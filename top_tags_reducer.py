#!/usr/bin/python

# Reducer

import sys

tags = {}

print "Tag |", "\t", "Counts"

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue

	node_id, tagnames = data_mapped

	for tag in tagnames.strip().split():
		if tag not in tags:
			tags[tag] = 1
		else:
			tags[tag] += 1

# return top10 keys list  [0:10)
top10 = sorted(tags, key=tags.get, reverse=True)[:10]
for tag in top10:
	print tag, "\t", tags[tag]