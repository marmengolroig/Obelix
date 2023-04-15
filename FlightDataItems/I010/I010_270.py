# Track Number - I010/270
# Fixed length: 2 octets

from ClassLibrary.utils import *

class I010_270():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I010/270'
        self.parent.long = self.set_long()
        self.parent.length_type = 1 # 0: fixed, 1: extended, 2: repetitive, 3: compound
        self.parent.dataitem = self
        self.data = self.set_data()
        self.decoded_data = self.decode_data()


    def set_long(self):
        i = 0
        while i < len(self.parent.data_list):
            if self.parent.data_list[i] % 2 ==  0:
                break
            i += 1
        return i + 1 
    
    def set_data(self):
        return self.parent.data_list[0:self.parent.long]
    
    def decode_data(self):
        bin_str = decimal_to_bin_str(self.data[0])
        length = int(bin_str[0:7],2)

        tuple = (length)


        if self.parent.long > 1:
            bin_str = decimal_to_bin_str(self.data[1])
            orientation = int(bin_str[0:7],2)*360/128

            tuple = (length, orientation)


        if self.parent.long > 2:
            bin_str = decimal_to_bin_str(self.data[2])
            width = int(bin_str[0:7],2)
        
            tuple = (length, orientation, width)
        
        return tuple
