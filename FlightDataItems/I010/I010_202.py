# Calculated Track Velocity in Cartesian Co-ordinates - I010/202
# Fixed length: 4 octets

from ClassLibrary.utils import *

class I010_202():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I010/202'
        self.parent.long = self.set_long()
        self.parent.length_type = 0 # 0: fixed, 1: extended, 2: repetitive, 3: compound
        self.parent.dataitem = self
        self.data = self.set_data()
        self.decoded_data = self.decode_data()


    def set_long(self):
        return 4
    
    def set_data(self):
        return self.parent.data_list[0:self.parent.long]
    
    def decode_data(self):
        vx = decimal_to_bin_str(self.data[0])+decimal_to_bin_str(self.data[1])
        vx = read_in_twos_complement(vx)*0.25  # m/s
        vy = decimal_to_bin_str(self.data[2])+decimal_to_bin_str(self.data[3])
        vy = read_in_twos_complement(vy)*0.25  # m/s
        return (vx,vy)
