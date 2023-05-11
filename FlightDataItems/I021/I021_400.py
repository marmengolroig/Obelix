# Receiver ID - I021/400
# Fixed length: 1 octets

from ClassLibrary.utils import *

class I021_400():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I021/400'
        self.parent.long = self.set_long()
        self.parent.length_type = 0 # 0: fixed, 1: extended, 2: repetitive, 3: compound
        self.parent.dataitem = self
        self.data = self.set_data()
        self.decoded_data = self.decode_data()

    def set_long(self):
        return 1
    
    def set_data(self):
        return self.parent.data_list[0:self.parent.long]
    
    def decode_data(self):
        
        return self.data[0]