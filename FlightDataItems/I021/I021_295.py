# Receiver ID - I021/295
# Compound length

from ClassLibrary.utils import *

class I021_295():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I021/295'
        self.parent.long = self.set_long()
        self.parent.length_type = 3 # 0: fixed, 1: extended, 2: repetitive, 3: compound
        self.parent.dataitem = self
        self.data = self.set_data()
        self.decoded_data = self.decode_data()
        self.subfield_list = [AOS,TRD,M3A,QI,TI1,MAM,GH,FX1,FL,ISA,FSA,AS,TAS,MH,BVR,FX2,GVR,GV,TAR,TI2,TS,MET,ROA,FX3,ARA,SCC]
        self.present_subfield_list = []

    def set_long(self):
        binary = self.parent.data_list[0:4]
        long = 4
        i = 0
        while i < len(binary):

            if binary[i] == '1':
                if int(binary[i]) % 8 != 0:
                    long += 1
                    self.present_subfield_list.append(i)

            i += 1
        return long
    
    def set_data(self):
        return self.parent.data_list[0:self.parent.long]
    
    def decode_data(self):
        
        i = 0
        while i < len(self.subfield_list):
            if self.subfield_list(i)

        return 