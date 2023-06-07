# Presence - (I010/280)
# Repetitive length.

from ClassLibrary.utils import *


class I010_280():
    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I010/280'
        self.parent.long = self.set_long()
        self.parent.length_type = 2 # 0: fixed, 1: extended, 2: repetitive, 3: compound
        self.parent.dataitem = self
        self.data = self.set_data()
        self.decoded_data = self.decode_data()

    def set_long(self):
        REP = self.parent.data_list[0]
        return 2*REP
                
    def set_data(self):
        return self.parent.data_list[0:self.parent.long]
    
    def decode_data(self):
        list = []
        i = 0
        while i < self.parent.long:
            binary = concatenate_decimals_in_binary(self.data[i:i+2])
            drho = int(binary[0:8],2)               # m
            dtheta = int(binary[8:16],2) * 0.15     # º
            list.append((drho,dtheta))
            i=i+2
        return list
