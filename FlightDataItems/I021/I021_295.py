# Data Ages - I021/295
# Compound length
from ClassLibrary.utils import *

class I021_295():

    def __init__(self, parent):
        self.subfield_list = []
        self.parent = parent
        self.parent.ref_no = 'I021/295'
        self.parent.long = self.set_long()
        self.parent.length_type = 3 # 0: fixed, 1: extended, 2: repetitive, 3: compound
        self.parent.dataitem = self
        self.data = self.set_data()
        self.decoded_data = self.decode_data()
    

    def set_long(self):
        #self.subfield_list = []
        primary_long = 0
        for decimal in self.parent.data_list[0:4]:
            primary_long = primary_long + 1
            if decimal % 2 == 0:
                break
        binary = concatenate_decimals_in_binary(self.parent.data_list[0:primary_long])
        long = primary_long
        i = 0
        while i < len(binary):

            if binary[i] == '1':
                if (i+1) % 8 != 0:
                    long += 1
                    self.subfield_list.append(1)
            else:
                if (i+1) % 8 != 0:
                    long += 1
                    self.subfield_list.append(-1)
            i += 1
        return long
    
    def set_data(self):
        return self.parent.data_list[0:self.parent.long]
    
    def decode_data(self):
        primary_long = 0
        for decimal in self.parent.data_list[0:4]:
            primary_long = primary_long + 1
            if decimal % 2 == 0:
                break
        binary = concatenate_decimals_in_binary(self.data[primary_long:self.parent.long])

        i = 0
        j = 0
        while i < len(self.subfield_list):
            if self.subfield_list[i] == 1:
                subfield = binary[j:j+8]
                self.subfield_list[i] = int(subfield, 2)*0.1
                j+=8
            i+=1

        return self.subfield_list
