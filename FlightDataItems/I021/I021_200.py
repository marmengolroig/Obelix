# Target Status - I021/200
# Fixed length: 1 octets

from ClassLibrary.utils import *

class I021_200():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I021/200'
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
        binary=decimal_to_bin_str(self.data[0])
        ICF = binary[0]
        if ICF == '0':
            ICF = 'No intent change active'
        elif ICF == '1':
            ICF = 'Intent change flag raised'

        LNAV = binary[1]
        if LNAV == '0':
            LNAV = 'LNAV Mode engaged'
        elif LNAV == '1':
            LNAV = 'LNAV Mode not engaged'

        PS = binary[3:6]
        if PS == '000':
            PS = 'No emergency / not reported'
        elif PS == '001':
            PS = 'General emergency'
        elif PS == '010':
            PS = 'Lifeguard / medical emergency'
        elif PS == '011':
            PS = 'Minimum fuel'
        elif PS == '100':
            PS = 'No communications'
        elif PS == '101':
            PS = 'Unlawful interference'
        elif PS == '110':
            PS = '"Downed" aircraft'
        
        SS = binary[6:8]
        if SS == '00':
            SS = 'No condition reported'
        elif SS == '01':
            SS = 'Permanent Alert (Emergency condition)'
        elif SS == '10':
            SS = 'Temporary Alert (change in Mode 3/A Code other than emergency)'
        elif SS == '11':
            SS = 'SPI set'
        
        return (ICF, LNAV, PS, SS)