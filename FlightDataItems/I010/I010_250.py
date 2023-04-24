# Mode S MB Data - I010/250
# Repetitive

from ClassLibrary.utils import *

class I010_250():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I010/250'
        self.parent.long = self.set_long()
        self.parent.length_type = 2 # 0: fixed, 1: extended, 2: repetitive, 3: compound
        self.parent.dataitem = self
        self.data = self.set_data()
        self.decoded_data = self.decode_data()


    def set_long(self):
        return (1 + int(self.parent.data_list[0],2))
    
    def set_data(self):
        return self.parent.data_list[0:self.parent.long]
    
    def decode_data(self):
        return ()
