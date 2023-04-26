# Selected Altitude - I021/146
# Fixed length: 2 octets

from ClassLibrary.utils import *

class I021_146():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I021/146'
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
        binary = concatenate_decimals_in_binary(self.data)
        SAS = binary[0]
        if SAS == '0':
            SAS = 'No source information provided'
        elif SAS == '1':
            SAS = 'Source information provided'
        
        Source = binary[1:3]
        if Source == '00':
            Source = 'Unknown'
        elif Source == '01':
            Source = 'Aircraft Altitude (Holding Altitude)'
        elif Source == '10':
            Source = 'MCP/FCU Selected Altitude'
        elif Source == '11':
            Source = 'FMS Selected Altitude'

        altitude = read_in_twos_complement(binary[3:16])*25
        
        return (SAS, Source, altitude)