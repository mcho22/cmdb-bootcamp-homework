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
        temp_number_2 = 0
        temp_number_3 = 0
        
        while True:
            line = sys.stdin.readline()
            if line.startswith( "Gap" ) and not line.startswith( "Gapped" ):
                raise StopIteration
            elif line.startswith( "Query=" ):
                self.last_flyid = line[7:24].rstrip("\r\n") + "\t"
            elif line.startswith( "> N" ):
                self.last_humanid = line[2:-3].rstrip("\r\n") + "\t"
            elif line.startswith( " Iden"):
                temp_number = len(''.join(x for x in line[-5:] if x.isdigit()))
                iden_gap = line[14:-4-temp_number].rstrip("\r\n")
                temp_number = len(''.join(x for x in iden_gap[-8:] if x.isdigit()))
                temp_number_2 = len(''.join(x for x in iden_gap[:8] if x.isdigit()))
                temp_number_3 = len(''.join(x for x in iden_gap[:4] if x.isdigit()))
                if temp_number_3 == 4:
                    temp_number_2 += 2
                iden = iden_gap[:temp_number_2+1].strip()
                gap = iden_gap[min(-4, -temp_number-3):].strip()
                break

        sequence = self.last_flyid + self.last_humanid + iden + "\t" + gap
        return sequence
        
    def __iter__( self ):
        return self