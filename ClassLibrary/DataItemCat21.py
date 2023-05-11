# A class "DataItem" is declared with its attributes:
# REF_NO- is the identifier of the data item,
# LONG - is the length of the data item in octets,

from FlightDataItems.I021.I021_010 import I021_010
from FlightDataItems.I021.I021_040 import I021_040
from FlightDataItems.I021.I021_161 import I021_161
from FlightDataItems.I021.I021_015 import I021_015
from FlightDataItems.I021.I021_130 import I021_130
from FlightDataItems.I021.I021_131 import I021_131
from FlightDataItems.I021.I021_080 import I021_080
from FlightDataItems.I021.I021_073 import I021_073
from FlightDataItems.I021.I021_075 import I021_075
from FlightDataItems.I021.I021_140 import I021_140
from FlightDataItems.I021.I021_090 import I021_090
from FlightDataItems.I021.I021_210 import I021_210
from FlightDataItems.I021.I021_070 import I021_070
from FlightDataItems.I021.I021_145 import I021_145
from FlightDataItems.I021.I021_200 import I021_200
from FlightDataItems.I021.I021_155 import I021_155
from FlightDataItems.I021.I021_160 import I021_160
from FlightDataItems.I021.I021_077 import I021_077
from FlightDataItems.I021.I021_170 import I021_170
from FlightDataItems.I021.I021_020 import I021_020
from FlightDataItems.I021.I021_146 import I021_146
from FlightDataItems.I021.I021_016 import I021_016
from FlightDataItems.I021.I021_008 import I021_008
from FlightDataItems.I021.I021_132 import I021_132
from FlightDataItems.I021.I021_400 import I021_400
from FlightDataItems.I021.I021_295 import I021_295
from FlightDataItems.I021.I021_RE import I021_RE
from FlightDataItems.I021.I021_071 import I021_071
from FlightDataItems.I021.I021_271 import I021_271


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
        elif self.FRN == 5:
            return I021_071(self)
        elif self.FRN == 6:
            return I021_130(self)
        elif self.FRN == 7:
            return I021_131(self)
        elif self.FRN == 11:
            return I021_080(self)
        elif self.FRN == 12:
            return I021_073(self)
        elif self.FRN == 14:
            return I021_075(self)
        elif self.FRN == 16:
            return I021_140(self)
        elif self.FRN == 17:
            return I021_090(self)
        elif self.FRN == 18:
            return I021_210(self)
        elif self.FRN == 19:
            return I021_070(self)
        elif self.FRN == 21:
            return I021_145(self)
        elif self.FRN == 23:
            return I021_200(self)
        elif self.FRN == 24:
            return I021_155(self)
        elif self.FRN == 26:
            return I021_160(self)
        elif self.FRN == 28:
            return I021_077(self)
        elif self.FRN == 29:
            return I021_170(self)
        elif self.FRN == 30:
            return I021_020(self)
        elif self.FRN == 32:
            return I021_146(self)
        elif self.FRN == 35:
            return I021_016(self)
        elif self.FRN == 36:
            return I021_008(self)
        elif self.FRN == 37:
            return I021_271(self)
        elif self.FRN == 38:
            return I021_132(self)
        elif self.FRN == 41:
            return I021_400(self)
        elif self.FRN == 42:
            return I021_295(self)
        elif self.FRN == 48:
            return I021_RE(self)
        
        
    def retrieve_datalist(self):
        return self.data_list
    def retrieve_data(self):
        return self.dataitem.data
    