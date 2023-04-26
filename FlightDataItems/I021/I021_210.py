# Time of Message Reception for Velocity - I021/210
# Fixed length: 1 octets

from ClassLibrary.utils import *

class I021_210():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I021/210'
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
        print(self.data)
        binary=decimal_to_bin_str(self.data[0])
        VNS = binary[1]
        if VNS == '0':
            VNS = 'The MOPS Version is supported by the GS'
        elif VNS == '1':
            VNS = 'The MOPS Version is not supported by the GS'
        
        VN = binary[2:5]
        if VN == '000':
            VN = 'ED102/DO-260 [Ref. 8]'
        elif VN == '001':
            VN = 'DO-260A [Ref. 9]'
        elif VN == '010':
            VN = 'ED120A/DO-260B [Ref. 11]'
        
        LTT = binary[5:8]
        if LTT == '000':
            LTT = 'Other'
        elif LTT == '001':
            LTT = 'UAT'
        elif LTT == '010':
            LTT = '1090 ES'
        elif LTT == '011':
            LTT = 'VDL 4'
        else:
            LTT = 'Not assigned'
        
        return (VNS, VN, LTT)