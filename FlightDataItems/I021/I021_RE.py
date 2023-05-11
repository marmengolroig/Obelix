# Reserved Expansion Field - I021/RE
# Variable length

from ClassLibrary.utils import *

class I021_RE():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'RE'
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
    
    def get_data(self):
        return self.data
    
    def decode_data(self):
        return 'Reserved Expansion Field'