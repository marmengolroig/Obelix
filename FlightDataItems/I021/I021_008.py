# Service Management - I021/008
# Fixed length: 1 octets

from ClassLibrary.utils import *

class I021_008():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I021/008'
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
        binary = decimal_to_bin_str(self.data[0])
        RA=binary[0]
        if RA == '0':
            RA = 'TCAS II or ACAS RA not active'
        elif RA == '1':
            RA = 'TCAS RA active'

        TC=binary[1:3]
        if TC == '00':
            TC = 'no capability for Trajectory Change Reports'
        elif TC == '01':
            TC = 'support for TC+0 reports only'
        elif TC == '10':
            TC = 'support for multiple TC reports'
        elif TC == '11':
            TC = 'reserved'

        TS=binary[3]
        if TS == '0':
            TS = 'no capability to support Target State Reports'
        elif TS == '1':
            TS = 'capable of supporting target State Reports'

        ARV=binary[4]
        if ARV == '0':
            ARV = 'no capability to generate ARV-reports'
        elif ARV == '1':
            ARV = 'capable of generate ARV-reports'

        CDTIA=binary[5]
        if CDTIA == '0':
            CDTIA = 'CDTI not operational'
        elif CDTIA == '1':
            CDTIA = 'CDTI operational'

        Not_TCAS=binary[6]
        if Not_TCAS == '0':
            Not_TCAS = 'TCAS operational'
        elif Not_TCAS == '1':
            Not_TCAS = 'TCAS not operational'

        SA=binary[7]
        if SA == '0':
            SA = 'Antenna Diversity'
        elif SA == '1':
            SA = 'Single Antenna only'
        
        return (RA, TC, TS, ARV, CDTIA, Not_TCAS, SA)