import sys
import re

class BLASTReader(object):
    def __init__( self, file ):
        
        self.file = file
        self.last_flyid = None
        self.last_humanid = None
        
    def next( self ):
        
        if self.last_flyid is None:
            line = sys.stdin.readline()
            assert line.startswith( "BLASTN" )
            sid = line.rstrip("\r\n")
        else:
            sid = self.last_flyid
        
        iden_gap = ""
        iden = ""
        gap = ""
        temp_number = 0
        l1 = ""
        l2 = ""
        l3 = ""
        l1_list = []
        l2_list = []
        l3_list = []
        
        l2_cutter = 0
        
        while True:
            line = sys.stdin.readline()
            if line.startswith( "Gap" ) and not line.startswith( "Gapped" ):
                raise StopIteration
            elif line.startswith( "Query=" ):
                self.last_flyid = line.split()[2] + "\t"
            elif line.startswith( "> N" ):
                self.last_humanid = line.split()[1] + "\t"
            elif line.startswith( " Iden"):
                iden = line.split()[2] + "\t"
                gap = line.split()[6] # + "\t"
                temp_number = (int(iden[int(len(iden))/2:]) - 1) / 60 + 1

            elif line.startswith( "Query"):
                l1 = line.split()[2]
                l1_list.append(l1)
                l2_cutter = 9+len(line.split()[1])
                if line[l2_cutter] == " ":
                    l2_cutter += 1
            elif line.startswith( "            ") and not line.startswith("                                                                      Score") :
                l2 = line[l2_cutter:].rstrip("\n")
                l2_list.append(l2)
            elif line.startswith( "Sbjct"):
                l3 = line.split()[2]
                l3_list.append(l3)
                if len(l3_list) == temp_number:
                    break
                
        l1 = "".join(l1_list)
        l2 = "".join(l2_list)
        l3 = "".join(l3_list)
        
        longest_match = 0
        longest_site = 0
        temp_i = 0
        counter_i = 1
        
        for i in l2:
            
            if i == "|":
                temp_i += 1
            else:
                if temp_i > longest_match:
                    longest_match = temp_i
                    longest_site = counter_i - temp_i-1
                temp_i = 0
            counter_i += 1
        
        if temp_i > longest_match:
            longest_match = temp_i
            longest_site = counter_i - temp_i-1
        
        longest_full_alignment = l1[longest_site:longest_site+longest_match] + " " + str(longest_site+1) + " - " + str(longest_site+longest_match) + "\n" + l2[longest_site:longest_site+longest_match] + " " + str(longest_match) + " bp" + "\n" + l3[longest_site:longest_site+longest_match] + " " + str(longest_site+1) + " - " + str(longest_site+longest_match)
               
        sequence = self.last_flyid + self.last_humanid + iden + gap + "\n" + "[BLAST alignment result]" + "\n" + l1 + "\n" + l2 + "\n" + l3 
        return sequence, longest_full_alignment
        
    def __iter__( self ):
        return self