# A class "DataItem" is declared with its attributes:
# REF_NO- is the identifier of the data item,
# LONG - is the length of the data item in octets,

from FlightDataItems.I010.I010_010 import I010_010



class DataItem:
    def __init__(self, FRN, starting_octet):
        self.ref_no = ''
        self.FRN = FRN
        self.long = 0
        self.length_type = 0 # 0: fixed, 1: extended, 2: repetitive, 3: compound
        self.dataitem = self.create_dataitem()
        self.data = []
        self.starting_octet = starting_octet
        
    def retrieve_long(self):
        return self.long
    def retrieve_long_type(self):
        return self.length_type
    
    def set_long_type(self, type):
        self.length_type = self.dataitem.long_type

    def create_dataitem(self):
        # if self.FRN is 1:
        if self.FRN == 1:
            return I010_010(self)
        
    def set_data(self, data):
        self.data = data
    