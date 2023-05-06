# Track Number - I010/170
# Fixed length: 2 octets

from ClassLibrary.utils import *

class I010_170():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I010/170'
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
        CNF = bin_str[0]
        if CNF == '0':
            CNF = 'Confirmed track'
        else:
            CNF = 'Track in initialization phase'

        TRE = bin_str[1]
        if TRE == '0':
            TRE = 'Default'
        else:
            TRE = 'Last report for a track'

        CST = bin_str[2:4]
        if CST == '00':
            CST = 'No extrapolation'
        elif CST == '01':
            CST = 'Predictable extrapolation due to sensor refresh period'
        elif CST == '10':
            CST = 'Predictable extrapolation in masked area'
        elif CST == '11':
            CST = 'Extrapolation due to unpredictable absence of detection'

        MAH = bin_str[4]
        if MAH == '0':
            MAH = 'Default'
        else:
            MAH = 'Horizontal manoeuvre'

        TCC = bin_str[5]
        if TCC == '0':
            TCC = "Tracking performed in 'Sensor Plane', i.e. neither slant range correction nor projection was applied"
        else:
            TCC = 'Slant range correction and a suitable projection technique are used to track in a 2D.reference plane, tangential to the earth model at the Sensor Site co-ordinates'

        STH = bin_str[6]
        if STH == '0':
            STH = 'Measured position'
        else:
            STH = 'Smoothed position'

        tuple = (CNF, TRE, CST, MAH, TCC, STH)


        if self.parent.long > 1:
            bin_str = decimal_to_bin_str(self.data[1])
            TOM = bin_str[0:2]
            if TOM == '00':
                TOM = 'Unknown type of movement'
            elif TOM == '01':
                TOM = 'Taking-off'
            elif TOM == '10':
                TOM = 'Landing'
            elif TOM == '11':
                TOM = 'Other types of movement'

            DOU = bin_str[2:5]
            if DOU == '000':
                DOU = 'No doubt'
            elif DOU == '001':
                DOU = 'Doubtful correlation (undetermined reason)'
            elif DOU == '010':
                DOU = 'Doubtful correlation in clutter'
            elif DOU == '011':
                DOU = 'Loss of accuracy'
            elif DOU == '100':
                DOU = 'Loss of accuracy in clutter'
            elif DOU == '101':
                DOU = 'Unstable track'
            elif DOU == '110':
                DOU = 'Previously coasted'

            MRS = bin_str[5:7]
            if MRS == '00':
                MRS = 'Merge or split indication undetermined'
            elif MRS == '01':
                MRS = 'Track merged by association to plot'
            elif MRS == '10':
                MRS = 'Track merged by non-association to plot'
            elif MRS == '11':
                MRS = 'Split track'

            tuple =  (CNF, TRE, CST, MAH, TCC, STH, TOM, DOU, MRS)


            if self.parent.long > 2:
                bin_str = decimal_to_bin_str(self.data[2])
                GHO = bin_str[0]
                if GHO == '0':
                    GHO = 'Default'
                elif GHO == '1':
                    GHO = 'Ghost track'
                tuple =  (CNF, TRE, CST, MAH, TCC, STH, TOM, DOU, MRS, GHO)
        return tuple
