# Emitter Category - I021/020
# Fixed length: 1 octets

from ClassLibrary.utils import *

class I021_020():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I021/020'
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
        if self.data[0] == 0:
            msg='No ADS-B Emitter Category Information'
        elif self.data[0] == 1:
            msg='light aircraft <= 15500 lbs'
        elif self.data[0] == 2:
            msg='15500 lbs < small aircraft <75000 lbs'
        elif self.data[0] == 3:
            msg='75000 lbs < medium a/c < 300000 lbs'
        elif self.data[0] == 4:
            msg='High Vortex Large'
        elif self.data[0] == 5:
            msg='300000 lbs <= heavy aircraft'
        elif self.data[0] == 6:
            msg='highly manoeuvrable (5g acceleration capability) and high speed (>400 knots cruise)'
        elif self.data[0] == 7:
            msg='reserved'
        elif self.data[0] == 8:
            msg='reserved'
        elif self.data[0] == 9:
            msg='reserved'
        elif self.data[0] == 10:
            msg='rotocraft'
        elif self.data[0] == 11:
            msg='glider / sailplane'
        elif self.data[0] == 12:
            msg='lighter-than-air'
        elif self.data[0] == 13:
            msg='unmanned aerial vehicle'
        elif self.data[0] == 14:
            msg='space / transatmospheric vehicle'
        elif self.data[0] == 15:
            msg='ultralight / handglider / paraglider'
        elif self.data[0] == 16:
            msg='parachutist / skydiver'
        elif self.data[0] == 17:
            msg='reserved'
        elif self.data[0] == 18:
            msg='reserved'
        elif self.data[0] == 19:
            msg='reserved'
        elif self.data[0] == 20:
            msg='surface emergency vehicle'
        elif self.data[0] == 21:
            msg='surface service vehicle'
        elif self.data[0] == 22:
            msg='fixed ground or tethered obstruction'
        elif self.data[0] == 23:
            msg='cluster obstacle'
        elif self.data[0] == 24:
            msg='line obstacle'

        
        return msg