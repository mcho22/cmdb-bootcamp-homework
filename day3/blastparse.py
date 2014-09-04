#!/usr/bin/env python

"""
Parse a single FASTA record from stdin and print it
"""

# Module import section

import sys

from blastread import BLASTReader

reader = BLASTReader( sys.stdin )
for sequence in reader:
    print sequence
