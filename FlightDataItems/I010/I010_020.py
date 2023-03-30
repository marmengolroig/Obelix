# Target Report Descriptor (TRD) - (I010/020)
# Extended length.

from ClassLibrary.utils import *


class I010_020():
    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I010/020'
        self.parent.long = self.set_long()
        self.parent.length_type = 1 # 0: fixed, 1: extended, 2: repetitive, 3: compound
        self.parent.dataitem = self
        self.data = self.set_data()
        self.decoded_data = self.decode_data()

    def set_long(self):
        i = 0
        while i < len(self.parent.data_list):
            if self.parent.data_list[i] % 2 ==  0:
                break
            i += 1
        return i + 1   
                
    def set_data(self):
        return self.parent.data_list[0:self.parent.long]
    
    def decode_data(self):
        bin_str = decimal_to_bin_str(self.data[0])
        TYP = bin_str[0:3]
        DCR = bin_str[3]
        CHN = bin_str[4]
        GBS = bin_str[5]
        CRT = bin_str[6]
        tuple = (TYP, DCR, CHN, GBS, CRT)
        if self.parent.long > 1:
            bin_str = decimal_to_bin_str(self.data[1])
            SIM = bin_str[0]
            TST = bin_str[1]
            RAB = bin_str[2]
            LOP = bin_str[3]
            TOT = bin_str[4:8]
            tuple =  (TYP, DCR, CHN, GBS, CRT, SIM, TST, RAB, LOP, TOT)
            if self.parent.long > 2:
                bin_str = decimal_to_bin_str(self.data[2])
                SPI = bin_str[0]
                tuple =  (TYP, DCR, CHN, GBS, CRT, SIM, TST, RAB, LOP, TOT, SPI)
        return tuple
        
                