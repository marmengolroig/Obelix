# Position in WGS-84 Co-ordinates - I010/060
# Fixed length: 2 octets

from ClassLibrary.utils import *

class I010_060():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I010/060'
        self.parent.long = self.set_long()
        self.parent.length_type = 0 # 0: fixed, 1: extended, 2: repetitive, 3: compound
        self.parent.dataitem = self
        self.data = self.set_data()
        self.decoded_data = self.decode_data()

    def set_long(self):
        return 2
    
    def set_data(self):
        return self.parent.data_list[0:self.parent.long]
    
    def decode_data(self):
        print(self.data)
        binary = concatenate_decimals_in_binary(self.data[0:4])

        V = binary[0]
        if V == '0':
            V = 'Code validated'
        elif V == '1':
            V = 'Code not validated'
        
        G = binary[1]
        if G == '0':
            G = 'Default'
        elif G == '1':
            G = 'Garbled Code'

        L = binary[2]
        if L == '0':
            L = 'Mode-3/A code derived from the reply of the transponder'
        elif L == '1':
            L = 'Mode-3/A code not extracted during the last scan'

        octal_reply = oct(int(binary[4:16],2))

        return (V, G, L, octal_reply)
    