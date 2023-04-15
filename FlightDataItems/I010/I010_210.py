# Calculated Acceleration - I010/210
# Fixed length: 2 octets

from ClassLibrary.utils import *

class I010_210():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I010/210'
        self.parent.long = self.set_long()
        self.parent.length_type = 0 # 0: fixed, 1: extended, 2: repetitive, 3: compound
        self.parent.dataitem = self
        self.data = self.set_data()
        self.decoded_data = self.decode_data()


    def set_long(self):
        return 2
    
    def set_data(self):
        return self.parent.data_list[0:self.parent.long]
    
    def decode_data(self):
        ax = read_in_twos_complement(decimal_to_bin_str(self.data[0]))*0.25
        ay = read_in_twos_complement(decimal_to_bin_str(self.data[1]))*0.25
        return (ax, ay)
