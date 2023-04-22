# CAT 21
# Target Report Descriptor (TRD) - (I021/040)
# Extended length.

from ClassLibrary.utils import *


class I021_040():
    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I021/040'
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
        bin_str = decimal_to_bin_str(self.data[0])

        ATP = bin_str[0:3] # Address Type
        if ATP == '000':
            ATP = '24-Bit ICAO Address'
        elif ATP == '001':
            ATP = 'Duplicate Address'
        elif ATP == '010':
            ATP = 'Surface Vehicle Address'
        elif ATP == '011':
            ATP = 'Anonymous Address'
        else:
            ATP = 'Reserved for future use'
        ARC = bin_str[3:5] # Altitude Reporting Capability
        if ARC == '00':
            ARC = '25 ft'
        elif ARC == '01':
            ARC = '100 ft'
        elif ARC == '10':
            ARC = 'Unknown'
        elif ARC == '11':
            ARC = 'Invalid'
        RC = bin_str[5] # Range Check
        if RC == '0':
            RC = 'Default'
        elif RC == '1':
            RC = 'Range Check passed, CPR Validation pending'
        RAB = bin_str[6] # Report Type
        if RAB == '0':
            RAB = 'Report from target transponder'
        elif RAB == '1':
            RAB = 'Report from field monitor (fixed transponder) '
        tuple = (ATP, ARC, RC, RAB)

        if self.parent.long > 1:
            bin_str = decimal_to_bin_str(self.data[1])

            DCR = bin_str[0] # Differential Correction
            if DCR == '0':
                DCR = 'No differential correction (ADS-B)'
            elif DCR == '1':
                DCR = 'Differential correction (ADS-B)'
            GBS = bin_str[1] # Ground Bit Setting
            if GBS == '0':
                GBS = 'Ground bit not set'
            elif GBS == '1':
                GBS = 'Ground bit set'
            SIM = bin_str[2] # Simulated Target
            if SIM == '0':
                SIM = 'Actual target report'
            elif SIM == '1':
                SIM = 'Simulated target report'
            TST = bin_str[3] # Test Target
            if TST == '0':
                TST = 'Default'
            elif TST == '1':
                TST = 'Test target'
            SAA = bin_str[4] # Selected Altitude Available
            if SAA == '0':
                SAA = 'Equipment capable to provide Selected Altitude'
            elif SAA == '1':
                SAA = 'Equipment not capable to provide Selected Altitude'
            CL = bin_str[5:7] # Confidence Level
            if CL == '00':
                CL = 'Report Valid'
            elif CL == '01':
                CL = 'Report suspect'
            elif CL == '10':
                CL = 'No information'
            elif CL == '11':
                CL = 'Reserved for future use'

            tuple =  (ATP, ARC, RC, RAB, DCR, GBS, SIM, TST, SAA, CL)

            if self.parent.long > 2:
                bin_str = decimal_to_bin_str(self.data[2])

                IPC = bin_str[2] # Independent Position Check
                if IPC == '0':
                    IPC = 'Default (see note)'
                elif IPC == '1':
                    IPC = 'Independent Position Check failed'
                NOGO = bin_str[3] # No-Go Bit Status
                if NOGO == '0':
                    NOGO = 'No-Go bit not set'
                elif NOGO == '1':
                    NOGO = 'No-Go bit set'
                CPR = bin_str[4] # Compact Position Reporting
                if CPR == '0':
                    CPR = 'CPR Validation correct'
                elif CPR == '1':
                    CPR = 'CPR Validation failed'
                LDPJ = bin_str[5] # Local Decoding Position Jump
                if LDPJ == '0':
                    LDPJ = 'LDPJ not detected'
                elif LDPJ == '1':
                    LDPJ = 'LDPJ detected'
                RCF = bin_str[6] # Range Check
                if RCF == '0':
                    RCF = 'Default'
                elif RCF == '1':
                    RCF = 'Range Check failed'

                tuple =  (ATP, ARC, RC, RAB, DCR, GBS, SIM, TST, SAA, CL, IPC, NOGO, CPR, LDPJ, RCF)
                
        return tuple
        