# Amplitude of Primary Plot - I010/131
# Fixed length: 1 octets

from ClassLibrary.utils import *

class I010_131():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I010/131'
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
        PAM = self.data[0]

        return PAM
