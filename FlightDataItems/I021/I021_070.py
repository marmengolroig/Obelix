# Mode 3/A Code in Octal Representation - I021/070
# Fixed length: 2 octets

from ClassLibrary.utils import *

class I021_070():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I021/070'
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
        decimal = int(binary[4:16],2)
        octal = decimal_to_four_digit_octal(decimal)
        
        return (octal)