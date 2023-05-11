# Target Identification - I021/170
# Fixed length: 6 octets

from ClassLibrary.utils import *

class I021_170():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I021/170'
        self.parent.long = self.set_long()
        self.parent.length_type = 0 # 0: fixed, 1: extended, 2: repetitive, 3: compound
        self.parent.dataitem = self
        self.data = self.set_data()
        self.decoded_data = self.decode_data()

    def set_long(self):
        return 6
    
    def set_data(self):
        return self.parent.data_list[0:self.parent.long]
    
    def decode_data(self):
        binary=concatenate_decimals_in_binary(self.data)
        char1 = read_character(binary[0:6])
        char2 = read_character(binary[6:12])
        char3 = read_character(binary[12:18])
        char4 = read_character(binary[18:24])
        char5 = read_character(binary[24:30])
        char6 = read_character(binary[30:36])
        char7 = read_character(binary[36:42])
        char8 = read_character(binary[42:48])

        
        return (char1+char2+char3+char4+char5+char6+char7+char8)