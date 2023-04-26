# Time of Message Reception for Velocity - I021/090
# Fixed length: 3 octets

from ClassLibrary.utils import *

class I021_090():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I021/090'
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
        binary=decimal_to_bin_str(self.data[0])
        NUCr_NACv = int(binary[0:3],2)
        NUCpNIC = int(binary[3:7],2)

        tuple = (NUCr_NACv,NUCpNIC)


        if self.parent.long > 1:
            binary=decimal_to_bin_str(self.data[1])
            NICbaro = int(binary[0],2)
            SIL = int(binary[1:3],2)
            NACp = int(binary[3:7],2)

            tuple =  (NUCr_NACv,NUCpNIC,NICbaro,SIL,NACp)


            if self.parent.long > 2:
                binary = decimal_to_bin_str(self.data[2])
                SIL_ = binary[2]
                if SIL_ == '0':
                    SIL_ = 'measured per flight-hour'
                elif SIL_ == '1':
                    SIL_ = 'measured per sample'
                SDA = int(binary[3:5],2)
                GVA = int(binary[5:7],2)
                tuple =  (NUCr_NACv,NUCpNIC,NICbaro,SIL,NACp,SIL_,SDA,GVA)

                if self.parent.long > 3:
                    binary = decimal_to_bin_str(self.data[3])
                    PIC = int(binary[0:4],2)
                
                    tuple =  (NUCr_NACv,NUCpNIC,NICbaro,SIL,NACp,SIL_,SDA,GVA,PIC)
        
        return tuple