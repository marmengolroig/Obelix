# Vehicle Fleet Identification - I010/300
# Fixed length: 2 octets

from ClassLibrary.utils import *

class I010_300():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I010/300'
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
        VFI=self.data[0]
        msg = ''

        if VFI == 0:
            msg = 'Unknown'
        elif VFI == 1:
            msg = 'ATC equipment maintenance'
        elif VFI == 2:
            msg = 'Airport maintenance'
        elif VFI == 3:
            msg = 'Fire'
        elif VFI == 4:
            msg = 'Bird scarer'
        elif VFI == 5:
            msg = 'Snow plough'
        elif VFI == 6:
            msg = 'Runway sweeper'
        elif VFI == 7:
            msg = 'Emergency'
        elif VFI == 8:
            msg = 'Police'
        elif VFI == 9:
            msg = 'Bus'
        elif VFI == 10:
            msg = 'Tug (push/tow)'
        elif VFI == 11:
            msg = 'Grass cutter'
        elif VFI == 12:
            msg = 'Fuel'
        elif VFI == 13:
            msg = 'Baggage'
        elif VFI == 14:
            msg = 'Catering'
        elif VFI == 15:
            msg = 'Aircraft maintenance'
        elif VFI == 16:
            msg = 'Flyco (follow me)'
        else:
            msg = 'Decoder error: unable to decode Vehicle Fleet Identification'
        
        return (msg)
