#!/usr/bin/env python

"""
Parse a single FASTA record from stdin and print it
"""

# Module import section

import sys

from blastread_med import BLASTReader

reader = BLASTReader( sys.stdin )

for sequence, longest_full_alignment in reader:
    print sequence
    print "\n"
    print "[Longest Full Alignment Data]"
    print longest_full_alignment
    print "\n"
