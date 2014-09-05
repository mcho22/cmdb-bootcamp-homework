#!/usr/bin/env python

"""
Parse a single FASTA record from stdin and print it
"""

# Module import section

import sys
import operator

from fasta import FASTAReader

reader = FASTAReader( sys.stdin )

for sid, sequence in reader:
    
    print sid
    print sequence[:min(len(sequence), 500)]

