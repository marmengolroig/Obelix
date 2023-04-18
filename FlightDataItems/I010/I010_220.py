# Target Address - I010/220
# Fixed length: 2 octets

from ClassLibrary.utils import *

class I010_220():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I010/220'
        self.parent.long = self.set_long()
        self.parent.length_type = 0 # 0: fixed, 1: extended, 2: repetitive, 3: compound
        self.parent.dataitem = self
        self.data = self.set_data()
        self.decoded_data = self.decode_data()

    def set_long(self):
        return 3
    
    def set_data(self):
        return self.parent.data_list[0:self.parent.long]
    
    def decode_data(self):
        print(self.data)
        target_adress = concatenate_decimals_in_binary(self.data)
        return (target_adress)
    