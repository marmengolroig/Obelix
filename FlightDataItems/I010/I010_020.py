# CAT 10
# Target Report Descriptor (TRD) - (I010/020)
# Extended length.

from ClassLibrary.utils import *


class I010_020():
    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I010/020'
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
        print(self.data)
        bin_str = decimal_to_bin_str(self.data[0])
        TYP = bin_str[0:3]
        if TYP == '000':
            TYP = 'SSR multilateration'
        elif TYP == '001':
            TYP = 'Mode S Multilateration'
        elif TYP == '010':
            TYP = 'ADS-B'
        elif TYP == '011':
            TYP = 'PSR'
        elif TYP == '100':
            TYP = 'Magnetic Loop System'
        elif TYP == '101':
            TYP = 'HF Multilateration'
        elif TYP == '110':
            TYP = 'Not defined'
        elif TYP == '111':
            TYP = 'Other types'

        DCR = bin_str[3]
        if DCR == '0':
            DCR = 'No differential correction (ADS-B)'
        elif DCR == '1':
            DCR = 'Differential correction (ADS-B)'

        CHN = bin_str[4]
        if CHN == '0':
            CHN = 'Chain 1'
        elif CHN == '1':
            CHN = 'Chain 2'

        GBS = bin_str[5]
        if GBS == '0':
            GBS = 'Transponder Ground Bit not set'
        elif GBS == '1':
            GBS = 'Transponder Ground Bit set'

        CRT = bin_str[6]
        if CRT == '0':
            CRT = 'No Corrupted reply in multilateration'
        elif CRT == '1':
            CRT = 'Corrupted replies in multilateration'

        tuple = (TYP, DCR, CHN, GBS, CRT)
        if self.parent.long > 1:
            bin_str = decimal_to_bin_str(self.data[1])
            SIM = bin_str[0]
            if SIM == '0':
                SIM = 'Actual target report'
            elif SIM == '1':
                SIM = 'Simulated target report'

            TST = bin_str[1]
            if TST == '0':
                TST = 'Default'
            elif TST == '1':
                TST = 'Test target'

            RAB = bin_str[2]
            if RAB == '0':
                RAB = 'Report from target transponder'
            elif RAB == '1':
                RAB = 'Report from field monitor (fixed transponder)'

            LOP = bin_str[3]
            if LOP == '00':
                LOP = 'Undetermined'
            elif LOP == '01':
                LOP = 'Loop start'
            elif LOP == '10':
                LOP = 'Loop end'

            TOT = bin_str[4:8]
            if TOT == '00':
                TOT = 'Undetermined'
            elif TOT == '01':
                TOT = 'Aircraft'
            elif TOT == '10':
                TOT = 'Ground vehicle'
            elif TOT == '11':
                TOT = 'Helicopter'

            tuple =  (TYP, DCR, CHN, GBS, CRT, SIM, TST, RAB, LOP, TOT)
            if self.parent.long > 2:
                bin_str = decimal_to_bin_str(self.data[2])
                SPI = bin_str[0]
                if SPI == '0':
                    SPI = 'Absence of SPI'
                elif SPI == '1':
                    SPI = 'Special Position Identification'
                tuple =  (TYP, DCR, CHN, GBS, CRT, SIM, TST, RAB, LOP, TOT, SPI)
        return tuple
        
                