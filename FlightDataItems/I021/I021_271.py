# Surface Capabilities and Characteristics - I021/271
# Variable length

from ClassLibrary.utils import *

class I021_271():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I021/271'
        self.parent.long = self.set_long()
        self.parent.length_type = 1 # 0: fixed, 1: extended, 2: repetitive, 3: compound
        self.parent.dataitem = self
        self.data = self.set_data()
        self.decoded_data = self.decode_data()

    def set_long(self):
        i = 0
        while i < len(self.parent.data_list):
            if self.parent.data_list[i] % 2 ==  0:
                break
            i += 1
        return i + 1 
    
    def set_data(self):
        return self.parent.data_list[0:self.parent.long]
    
    def decode_data(self):
        binary=decimal_to_bin_str(self.data[0])
        POA = binary[2]
        if POA == '0':
            POA = 'Position transmitted is not ADS-B position reference point'
        elif POA == '1':
            POA = 'Position transmitted is the ADS-B position reference point'

        CDTIS = binary[3]
        if CDTIS == '0':
            CDTIS = 'CDTI not operational'
        elif CDTIS == '1':
            CDTIS = 'CDTI operational'

        B2_low = binary[4]
        if B2_low == '0':
            B2_low = '≥ 70 Watts'
        elif B2_low == '1':
            B2_low = '< 70 Watts'
        
        RAS = binary[5]
        if RAS == '0':
            RAS = 'Aircraft not receiving ATC-services'
        elif RAS == '1':
            RAS = 'Aircraft receiving ATC services'

        IDENT = binary[6]
        if IDENT == '0':
            IDENT = 'IDENT switch not active'
        elif IDENT == '1':
            IDENT = 'IDENT switch active'

        tuple = (POA, CDTIS, B2_low, RAS, IDENT)


        if self.parent.long > 1:
            binary=decimal_to_bin_str(self.data[1])
            LD = int(binary[4:8],2)
            if LD == 0:
                LD = 'L < 15; W < 11.5'
            elif LD == 1:
                LD = 'L < 15; W < 23'
            elif LD == 2:
                LD = 'L < 25; W < 28.5'
            elif LD == 3:
                LD = 'L < 25; W < 34'
            elif LD == 4:
                LD = 'L < 35; W < 33'
            elif LD == 5:
                LD = 'L < 35; W < 38'
            elif LD == 6:
                LD = 'L < 45; W < 39.5'
            elif LD == 7:
                LD = 'L < 45; W < 45'
            elif LD == 8:
                LD = 'L < 55; W < 45'
            elif LD == 9:
                LD = 'L < 55; W < 52'
            elif LD == 10:
                LD = 'L < 65; W < 59.5'
            elif LD == 11:
                LD = 'L < 65; W < 67'
            elif LD == 12:
                LD = 'L < 75; W < 72.5'
            elif LD == 13:
                LD = 'L < 75; W < 80'
            elif LD == 14:
                LD = 'L < 85; W < 80'
            elif LD == 15:
                LD = 'L < 85; W > 80'

            tuple =  (POA, CDTIS, B2_low, RAS, IDENT, LD)

        
        return tuple