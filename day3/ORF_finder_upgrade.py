#!/usr/bin/env python

"""
Parse a single FASTA record from stdin and print it
"""

# Module import section

import sys
import operator

from fasta import FASTAReader

reader = FASTAReader( sys.stdin )

# codon data

table = {"TTT ": "F ", "TTC ": "F ", "TTA ": "L ", "TTG ": "L ", "TCT ": "S ", "TCC ": "S ", "TCA ": "S ", "TCG ": "S ",
         "TAT ": "Y ", "TAC ": "Y ", "TAA ": "STOP ", "TAG ": "STOP ", "TGT ": "C ", "TGC ": "C ", "TGA ": "STOP ", "TGG ": "W ",
         "CTT ": "L ", "CTC ": "L ", "CTA ": "L ", "CTG ": "L ", "CCT ": "P ", "CCC ": "P ", "CCA ": "P ", "CCG ": "P ", 
         "CAT ": "H ", "CAC ": "H ", "CAA ": "Q ", "CAG ": "Q ", "CGT ": "R ", "CGC ": "R ", "CGA ": "R ", "CGG ": "R ", 
         "ATT ": "I ", "ATC ": "I ", "ATA ": "I ", "ATG ": "M ", "ACT ": "T ", "ACC ": "T ", "ACA ": "T ", "ACG ": "T ", 
         "AAT ": "N ", "AAC ": "N ", "AAA ": "K ", "AAG ": "K ", "AGT ": "S ", "AGC ": "S ", "AGA ": "R ", "AGG ": "R ", 
         "GTT ": "V ", "GTC ": "V ", "GTA ": "V ", "GTG ": "V ", "GCT ": "A ", "GCC ": "A ", "GCA ": "A ", "GCG ": "A ", 
         "GAT ": "D ", "GAC ": "D ", "GAA ": "E ", "GAG ": "E ", "GGT ": "G ", "GGC ": "G ", "GGA ": "G ", "GGG ": "G "}

new_table = {}

for key, value in table.iteritems():
    new_table[key.strip()] = value.strip()

# replication step

paired_s = []

for sid, sequence in reader:

    rep_temp = sequence
    
    rep_list = []
    for i in rep_temp:
        if i == "A":
            rep_list.insert(0, "T")
        elif i == "T":
            rep_list.insert(0, "A")
        elif i == "C":
            rep_list.insert(0, "G")
        elif i == "G":
            rep_list.insert(0, "C")
    paired_s.append(rep_temp)
    paired_s.append("".join(rep_list))

# frame setting step

framed_seq = []

for seq in paired_s:
    seq_temp = seq
    framed_list = []
    
    while len(seq_temp) >= 3:
        framed_list.append(seq_temp[:3])
        seq_temp = seq_temp[3:]
        
    framed_seq.append(framed_list)

    seq_temp = seq[1:]
    framed_list = []
    
    while len(seq_temp) >= 3:
        framed_list.append(seq_temp[:3])
        seq_temp = seq_temp[3:]
        
    framed_seq.append(framed_list)
    
    seq_temp = seq[1:]
    framed_list = []
    
    while len(seq_temp) >= 3:
        framed_list.append(seq_temp[:3])
        seq_temp = seq_temp[3:]
        
    framed_seq.append(framed_list)

# Start / stop codon finding

orf_list = []

for fn in range (len(framed_seq)):

#   gene number & frame number setting

    gn = "Gene No. #" + str(int(fn)/6 + 1) + " // "
    if int(fn)%6 == 0:
        gf = "Forward Frame #1 // "
    elif int(fn)%6 == 1:
        gf = "Forward Frame #2 // "
    elif int(fn)%6 == 2:
        gf = "Forward Frame #3 // "
    elif int(fn)%6 == 3:
        gf = "Reverse Frame #1 // "
    elif int(fn)%6 == 4:
        gf = "Reverse Frame #2 // "
    elif int(fn)%6 == 5:
        gf = "Reverse Frame #3 // "
    
#    if int(fn)%30 == 29:
#        print "Progress " + str((int(fn)/30+1)*5) + "% completed."
    
    i = 0
    orf_num = 1
    
    for codes in framed_seq[fn]:
        framed_seq_copy = framed_seq[fn]
        seq_orf = []
#        seq_prot = []
    
        if codes == "ATG":

            seq_orf.append(codes)
            start_site = i
            j = i
            for sites in framed_seq_copy[i:]:
                if sites == "TAA":
                    break
                elif sites == "TAG":
                    break
                elif sites == "TGA":
                    break
                else:
                    j += 1
                    
            seq_orf_str = "".join(framed_seq_copy[i:j])
            seq_prot_str = ""
        
            if j-i > 34:
                
                # Protein sequence translation section
                
                for bp in range( 0, len(seq_orf_str), 3 ):
                    codon = new_table[ seq_orf_str[bp:bp+3] ]
                    seq_prot_str += codon

                orf_list.append(str(gn + gf + "ORF_NO #" + str(orf_num) + " // Start " + str(i*3+fn%3) + " " + "".join(framed_seq_copy[i:j+1]) + " " + str(j*3+fn%3+2) + " Stop // Length = " + str((j*3+fn%3+3) - (i*3+fn%3)) + " bp // Expected protein sequence : " + seq_prot_str))
                
                orf_num += 1
            
        i += 1

print "Total ORFs = " + str(len(orf_list))
for lines in orf_list:
    print lines