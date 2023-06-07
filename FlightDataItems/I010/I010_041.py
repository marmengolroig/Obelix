# Position in WGS-84 Co-ordinates - I010/041
# Fixed length: 8 octets

from ClassLibrary.utils import *

class I010_041():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I010/041'
        self.parent.long = self.set_long()
        self.parent.length_type = 0 # 0: fixed, 1: extended, 2: repetitive, 3: compound
        self.parent.dataitem = self
        self.data = self.set_data()
        self.decoded_data = self.decode_data()

    def set_long(self):
        return 8
    
    def set_data(self):
        return self.parent.data_list[0:self.parent.long]
    
    def decode_data(self):
        
        latitude_WGS84 = int(concatenate_decimals_in_binary(self.data[0:4]),2)*180/(2**31)
        longitude_WGS84 = int(concatenate_decimals_in_binary(self.data[4:8]),2)*180/(2**31)
        return (latitude_WGS84, longitude_WGS84)
    