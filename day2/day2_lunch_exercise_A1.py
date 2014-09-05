#! /usr/bin/env python

sam_location = "/Users/cmdb/data/day1/tophat_results/accepted_hits.sam"

f = open ( sam_location )
counts = {}
types = []

for i, lines in enumerate (f):
    if i <= 10:
        fields = lines.rstrip("\r\n").split("\t")
        types.append(fields[3])
        counts[lines] = counts.get((types[int(i-1)]), 0) + 1
    elif i > 10:
        break

print counts

sorted_counts = list (counts.items())
sorted_counts.sort(lambda a,b: -cmp((a[1], a[0]), (b[1], b[0])))

#for lines, counts in sorted_counts:
#    print "%7d %s" % (counts, lines)