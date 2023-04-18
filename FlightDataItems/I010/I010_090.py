# Flight Level in Binary Representation - I010/090
# Fixed length: 2 octets

from ClassLibrary.utils import *

class I010_090():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I010/090'
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
        binary = concatenate_decimals_in_binary(self.data)

        V = binary[0]
        if V == '0':
            V = 'Code validated'
        elif V == '1':
            V = 'Code not validated'

        G = binary[1]
        if G == '0':
            G = 'Default'
        elif G == '1':
            G = 'Garbled Code'

        FL = int(self.data[2:16],2)/4
        
        return (V, G, FL)
