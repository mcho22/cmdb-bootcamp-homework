#!/usr/bin/env python

"""
Parse a single FASTA record from stdin and print it
"""

# Module import section

import sys
import operator

from fasta import FASTAReader

reader = FASTAReader( sys.stdin )

sequences_index = []

for sid, sequence in reader:

    sequences_index.append((sid, sequence, len(sequence)))
#    print sid, sequence, len(sequence)

sorted_index = sorted(sequences_index, key=operator.itemgetter(2), reverse = True)[:100]

for i in sorted_index:
    print i[0]
    print i[1]
