# Barometric Vertical Rate - I021/155
# Fixed length: 2 octets

from ClassLibrary.utils import *

class I021_155():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I021/155'
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
        binary=concatenate_decimals_in_binary(self.data)
        RE = binary[0]
        if RE == '0':
            RE = 'Value in defined range'
        elif RE == '1':
            RE = 'Value exceeds defined range'

        BVR = read_in_twos_complement(binary[1:16])*6.25  #ft/min
        
        return (RE,BVR)