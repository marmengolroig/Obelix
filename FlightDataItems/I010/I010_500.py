# Standard Deviation of Position - I010/500
# Fixed length: 4 octets

from ClassLibrary.utils import *

class I010_500():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I010/500'
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
        binary = concatenate_decimals_in_binary(self.data)
        sigmax = int(binary[0:8],2)*0.25
        sigmay = int(binary[8:16],2)*0.25
        sigmaxy = int(binary[16:32],2)*0.25

        return (sigmax, sigmay, sigmaxy)
