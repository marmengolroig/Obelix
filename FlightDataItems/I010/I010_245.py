# Target Identification - I010/245
# Fixed length: 7 octets

from ClassLibrary.utils import *

class I010_245():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I010/245'
        self.parent.long = self.set_long()
        self.parent.length_type = 0 # 0: fixed, 1: extended, 2: repetitive, 3: compound
        self.parent.dataitem = self
        self.data = self.set_data()
        self.decoded_data = self.decode_data()

    def set_long(self):
        return 7
    
    def set_data(self):
        return self.parent.data_list[0:self.parent.long]
    
    def decode_data(self):
        print(self.data)
        binary = concatenate_decimals_in_binary(self.data)
        STI = binary[0:2]
        if STI == '00':
            STI = 'Callsign or registration downlinked from transponder'
        elif STI == '01':
            STI = 'Callsign not downlinked from transponder'
        elif STI == '10':
            STI = 'Registration not downlinked from transponder'

        ch1=read_character(binary[8:14])
        ch2=read_character(binary[14:20])
        ch3=read_character(binary[20:26])
        ch4=read_character(binary[26:32])
        ch5=read_character(binary[32:38])
        ch6=read_character(binary[38:44])
        ch7=read_character(binary[44:50])
        ch8=read_character(binary[50:56])
        return (STI, ch1+ch2+ch3+ch4+ch5+ch6+ch7+ch8)
    