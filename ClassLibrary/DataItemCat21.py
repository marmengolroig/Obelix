# A class "DataItem" is declared with its attributes:
# REF_NO- is the identifier of the data item,
# LONG - is the length of the data item in octets,

from FlightDataItems.I021.I021_010 import I021_010
from FlightDataItems.I021.I021_040 import I021_040
from FlightDataItems.I021.I021_161 import I021_161
from FlightDataItems.I021.I021_015 import I021_015



class DataItemCat21:
    def __init__(self, FRN, data_list):
        self.ref_no = ''
        self.FRN = FRN
        self.long = 0
        self.length_type = 0 # 0: fixed, 1: extended, 2: repetitive, 3: compound
        self.data_list = data_list
        self.dataitem = self.create_dataitem()
        
        
    def retrieve_long(self):
        return self.long

    def create_dataitem(self):
        if self.FRN == 1:
            return I021_010(self)
        elif self.FRN == 2:
            return I021_040(self)
        elif self.FRN == 3:
            return I021_161(self)
        elif self.FRN == 4:
            return I021_015(self)
        
        
    def retrieve_datalist(self):
        return self.data_list
    def retrieve_data(self):
        return self.dataitem.data
    