#!/usr/bin/env python

"""
Parse a single FASTA record from stdin and print it
"""

# Module import section

import sys
import operator

from fasta import FASTAReader

reader = FASTAReader( sys.stdin )

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
    
    while len(seq_temp) > 3:
        framed_list.append(seq_temp[:3])
        seq_temp = seq_temp[3:]
        
    framed_seq.append(framed_list)

    seq_temp = seq[1:]
    framed_list = []
    
    while len(seq_temp) > 3:
        framed_list.append(seq_temp[:3])
        seq_temp = seq_temp[3:]
        
    framed_seq.append(framed_list)
    
    seq_temp = seq[1:]
    framed_list = []
    
    while len(seq_temp) > 3:
        framed_list.append(seq_temp[:3])
        seq_temp = seq_temp[3:]
        
    framed_seq.append(framed_list)

# Start / stop codon finding

orf_list = []

for fn in range (len(framed_seq)):

# gene number & frame number setting

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
        seq_prot = []
    
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
        
            if j-i > 34:
                
                # Protein sequence translation section
                
                for codon in framed_seq_copy[i:j]:
                
                    if codon == "TTT":
                        seq_prot.append("F")
                    elif codon == "TTC":
                        seq_prot.append("F")
                    elif codon == "TTA":
                        seq_prot.append("L")
                    elif codon == "TTG":
                        seq_prot.append("L")
                    elif codon == "CTT":
                        seq_prot.append("L")
                    elif codon == "CTC":
                        seq_prot.append("L")
                    elif codon == "CTA":
                        seq_prot.append("L")
                    elif codon == "CTG":
                        seq_prot.append("L")
                    elif codon == "ATT":
                        seq_prot.append("I")
                    elif codon == "ATC":
                        seq_prot.append("I")
                    elif codon == "ATA":
                        seq_prot.append("I")
                    elif codon == "ATG":
                        seq_prot.append("M")
                    elif codon == "GTT":
                        seq_prot.append("V")
                    elif codon == "GTC":
                        seq_prot.append("V")
                    elif codon == "GTA":
                        seq_prot.append("V")
                    elif codon == "GTG":
                        seq_prot.append("V")
                    elif codon == "TCT":
                        seq_prot.append("S")
                    elif codon == "TCC":
                        seq_prot.append("S")
                    elif codon == "TCA":
                        seq_prot.append("S")
                    elif codon == "TCG":
                        seq_prot.append("S")
                    elif codon == "CCT":
                        seq_prot.append("P")
                    elif codon == "CCC":
                        seq_prot.append("P")
                    elif codon == "CCA":
                        seq_prot.append("P")
                    elif codon == "CCG":
                        seq_prot.append("P")
                    elif codon == "ACT":
                        seq_prot.append("T")
                    elif codon == "ACC":
                        seq_prot.append("T")
                    elif codon == "ACA":
                        seq_prot.append("T")
                    elif codon == "ACG":
                        seq_prot.append("T")
                    elif codon == "GCT":
                        seq_prot.append("A")
                    elif codon == "GCC":
                        seq_prot.append("A")
                    elif codon == "GCA":
                        seq_prot.append("A")
                    elif codon == "GCG":
                        seq_prot.append("A")
                    elif codon == "TAT":
                        seq_prot.append("Y")
                    elif codon == "TAC":
                        seq_prot.append("Y")
                    elif codon == "CAT":
                        seq_prot.append("H")
                    elif codon == "CAC":
                        seq_prot.append("H")
                    elif codon == "CAA":
                        seq_prot.append("Q")
                    elif codon == "CAG":
                        seq_prot.append("Q")
                    elif codon == "AAT":
                        seq_prot.append("N")
                    elif codon == "AAC":
                        seq_prot.append("N")
                    elif codon == "AAA":
                        seq_prot.append("K")
                    elif codon == "AAG":
                        seq_prot.append("K")
                    elif codon == "GAT":
                        seq_prot.append("D")
                    elif codon == "GAC":
                        seq_prot.append("D")
                    elif codon == "GAA":
                        seq_prot.append("E")
                    elif codon == "GAG":
                        seq_prot.append("E")
                    elif codon == "TGT":
                        seq_prot.append("C")
                    elif codon == "TGC":
                        seq_prot.append("C")
                    elif codon == "TGG":
                        seq_prot.append("W")
                    elif codon == "CGT":
                        seq_prot.append("R")
                    elif codon == "CGC":
                        seq_prot.append("R")
                    elif codon == "CGA":
                        seq_prot.append("R")
                    elif codon == "CGG":
                        seq_prot.append("R")
                    elif codon == "AGT":
                        seq_prot.append("S")
                    elif codon == "AGC":
                        seq_prot.append("S")
                    elif codon == "AGA":
                        seq_prot.append("R")
                    elif codon == "AGG":
                        seq_prot.append("R")
                    elif codon == "GGT":
                        seq_prot.append("G")
                    elif codon == "GGC":
                        seq_prot.append("G")
                    elif codon == "GGA":
                        seq_prot.append("G")
                    elif codon == "GGG":
                        seq_prot.append("G")
                
                orf_list.append(str(gn + gf + "ORF_NO #" + str(orf_num) + " // Start " + str(i*3+fn%3) + " " + "".join(framed_seq_copy[i:j+1]) + " " + str(j*3+fn%3+2) + " Stop // Length = " + str((j*3+fn%3+3) - (i*3+fn%3)) + " bp // Expected protein sequence : " + "".join(seq_prot)))
                
                orf_num += 1
            
        i += 1

print "Total ORFs = " + str(len(orf_list))
for lines in orf_list:
    print lines