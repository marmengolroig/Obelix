# Position in Cartesian Co-ordinates - I010/042
# Fixed length: 4 octets

from ClassLibrary.utils import *

class I010_042():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I010/042'
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
        print(self.data)
        x_component = int(concatenate_decimals_in_binary(self.data[0:2]),2)
        y_component = int(concatenate_decimals_in_binary(self.data[2:4]),2)
        return (x_component, y_component)
    