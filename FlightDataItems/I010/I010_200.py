# Calculated Track Velocity in Polar Coodinates (CTV-P) - I010/200
# Fixed length: 4 octets

from ClassLibrary.utils import *

class I010_200():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I010/200'
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
        ground_speed = decimal_to_bin_str(self.data[0])+decimal_to_bin_str(self.data[1])
        ground_speed = int(ground_speed,2)*7200/(2*16384)  # kt
        track_angle = decimal_to_bin_str(self.data[2])+decimal_to_bin_str(self.data[3])
        track_angle = int(track_angle,2)*360/65536  # deg
        return (ground_speed,track_angle)
