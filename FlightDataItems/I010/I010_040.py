# Position in Polar Co-ordinates - I010/040
# Fixed length: 4 octets

from ClassLibrary.utils import *

class I010_040():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I010/040'
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
        # print(concatenate_decimals_in_binary(self.data[0:2]))
        rho = int(concatenate_decimals_in_binary(self.data[0:2]),2)
        theta = int(concatenate_decimals_in_binary(self.data[2:4]),2)*360/(65536)
        return (rho, theta)
    