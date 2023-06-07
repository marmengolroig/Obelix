# Position in WGS-84 Co-ordinates - I021/130
# Fixed length: 6 octets

from ClassLibrary.utils import *

class I021_130():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I021/130'
        self.parent.long = self.set_long()
        self.parent.length_type = 0 # 0: fixed, 1: extended, 2: repetitive, 3: compound
        self.parent.dataitem = self
        self.data = self.set_data()
        self.decoded_data = self.decode_data()

    def set_long(self):
        return 6
    
    def set_data(self):
        return self.parent.data_list[0:self.parent.long]
    
    def decode_data(self):
        latitude_WGS84 = read_in_twos_complement(concatenate_decimals_in_binary(self.data[0:3]))*180/8388608
        longitude_WGS84 = read_in_twos_complement(concatenate_decimals_in_binary(self.data[3:6]))*180/8388608
        return (latitude_WGS84, longitude_WGS84)
    