# Airborne Ground Vector - I021/160
# Fixed length: 4 octets

from ClassLibrary.utils import *

class I021_160():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I021/160'
        self.parent.long = self.set_long()
        self.parent.length_type = 0 # 0: fixed, 1: extended, 2: repetitive, 3: compound
        self.parent.dataitem = self
        self.data = self.set_data()
        self.decoded_data = self.decode_data()

    def set_long(self):
        return 4
    
    def set_data(self):
        return self.parent.data_list[0:self.parent.long]
    
    def decode_data(self):
        binary=concatenate_decimals_in_binary(self.data)
        RE = binary[0]
        if RE == '0':
            RE = 'Value in defined range'
        elif RE == '1':
            RE = 'Value exceeds defined range'

        GS = int(binary[1:16],2)/16384  #NM/s
        TA = int(binary[16:32],2)*360/65536 #º

        
        return (GS,TA)