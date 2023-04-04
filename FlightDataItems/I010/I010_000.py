# Message Type (MT) - (I010/000)
# Fixed length: 1 octet

from ClassLibrary.utils import *


class I010_000():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I010/000'
        self.parent.long = self.set_long()
        self.parent.length_type = 0 # 0: fixed, 1: extended, 2: repetitive, 3: compound
        self.parent.dataitem = self
        self.data = self.set_data()
        self.decoded_data = self.decode_data()
        # self.MTcode = self.decode_data()[0]
        # self.MTstring = self.decode_data()[1]

    def set_long(self):
        return 1
    
    def set_data(self):
        return self.parent.data_list[0:self.parent.long]
    
    def decode_data(self):
        MTstring = ''
        if self.data[0] == 1:
            MTstring = 'Target Report'
        elif self.data[0] == 2:
            MTstring = 'Start of Update Cycle'
        elif self.data[0] == 3:
            MTstring = 'Periodic Status Message'
        elif self.data[0] == 4:
            MTstring = 'Event Triggered Status Message'
        return MTstring
