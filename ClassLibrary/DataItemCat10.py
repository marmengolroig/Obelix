# A class "DataItem" is declared with its attributes:
# REF_NO- is the identifier of the data item,
# LONG - is the length of the data item in octets,

from FlightDataItems.I010.I010_010 import I010_010
from FlightDataItems.I010.I010_000 import I010_000
from FlightDataItems.I010.I010_020 import I010_020
from FlightDataItems.I010.I010_140 import I010_140
from FlightDataItems.I010.I010_040 import I010_040
from FlightDataItems.I010.I010_042 import I010_042
from FlightDataItems.I010.I010_200 import I010_200
from FlightDataItems.I010.I010_202 import I010_202
from FlightDataItems.I010.I010_161 import I010_161
from FlightDataItems.I010.I010_170 import I010_170
from FlightDataItems.I010.I010_270 import I010_270


class DataItemCat10:
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
            return I010_010(self)
        elif self.FRN == 2:
            return I010_000(self)
        elif self.FRN == 3:
            return I010_020(self)
        elif self.FRN == 4:
            return I010_140(self)
        elif self.FRN == 6:
            return I010_040(self)
        elif self.FRN == 7:
            return I010_042(self)
        elif self.FRN == 8:
            return I010_200(self)
        elif self.FRN == 9:
            return I010_202(self)
        elif self.FRN == 10:
            return I010_161(self)
        elif self.FRN == 11:
            return I010_170(self)
        elif self.FRN == 19:
            return I010_270(self)
        
    def retrieve_datalist(self):
        return self.data_list
    def retrieve_data(self):
        return self.dataitem.data
    