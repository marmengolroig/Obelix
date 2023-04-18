# Measured Height - I010/550
# Fixed length: 1 octets

from ClassLibrary.utils import *

class I010_550():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I010/550'
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
        binary = decimal_to_bin_str(self.data[0])
        NOGO = binary[0:2]
        if NOGO == '00':
            NOGO = 'Operational'
        elif NOGO == '01':
            NOGO = 'Degraded'
        elif NOGO == '10':
            NOGO = 'NOGO'
        OVL = binary[2]
        if OVL == '0':
            OVL = 'No overload'
        elif OVL == '1':
            OVL = 'Overload'
        TSV = binary[3]
        if TSV == '0':
            TSV = 'Valid'
        elif TSV == '1':
            TSV = 'Invalid'
        DIV = binary[4]
        if DIV == '0':
            DIV = 'Normal operation'
        elif DIV == '1':
            DIV = 'Diversity degraded'
        TTF = binary[5]
        if TTF == '0':
            TTF = 'Test Target Operative'
        elif TTF == '1':
            TTF = 'Test Target Failure'
        
        return (NOGO, OVL, TSV, DIV, TTF)
