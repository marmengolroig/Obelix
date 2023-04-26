# High-Resolution Position in WGS-84 Co-ordinates - I021/131
# Fixed length: 8 octets

from ClassLibrary.utils import *

class I021_131():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I021/131'
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
        print(self.data)
        latitude_WGS84 = read_in_twos_complement(concatenate_decimals_in_binary(self.data[0:4]))*180/1073741824  # 2^30
        longitude_WGS84 = read_in_twos_complement(concatenate_decimals_in_binary(self.data[4:8]))*180/1073741824 # 2^30
        return (latitude_WGS84, longitude_WGS84)
    