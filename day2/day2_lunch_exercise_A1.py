#! /usr/bin/env python

sam_location = "/Users/cmdb/data/day1/tophat_results/accepted_hits.sam"

f = open ( sam_location )
counts = {}

for lines in f:
    fields = lines.rstrip("\r\n").split("\t")
    counts[lines] = counts.get(lines, 0) + 1

sorted_counts = list (counts.items())
sorted_counts.sort(lambda a,b: -cmp((a[1], a[0]), (b[1], b[0])))

for line, count in sorted_counts:
    print "%7d %s" % (counts, lines)