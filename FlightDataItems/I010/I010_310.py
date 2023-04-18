# Pre-programmed Message - I010/310
# Fixed length: 1 octets

from ClassLibrary.utils import *

class I010_310():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I010/310'
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
        msg = ''
        binary = decimal_to_bin_str(self.data[0])
        TRB = binary[0]
        if TRB == '0':
            TRB = 'Default'
        elif TRB == '1':
            TRB = 'In trouble'
        MSG = int(binary[1:8],2)
        if MSG == 1:
            msg = 'Towing aircraft'
        elif MSG == 2:
            msg = '"Follow me" operation'
        elif MSG == 3:
            msg = 'Runway check'
        elif MSG == 4:
            msg = 'Emergency operation (fire, medical...)'
        elif MSG == 5:
            msg = 'Work in progress (maintenance, birds scarer, sweepers...)'

        return (TRB, msg)