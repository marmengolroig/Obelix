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
        data_item_map = {
            1: I021_010(self),
            2: I021_040(self),
            3: I021_161(self),
            4: I021_015(self),
            5: I021_071(self),
            6: I021_130(self),
            7: I021_131(self),
            11: I021_080(self),
            12: I021_073(self),
            14: I021_075(self),
            16: I021_140(self),
            17: I021_090(self),
            18: I021_210(self),
            19: I021_070(self),
            21: I021_145(self),
            23: I021_200(self),
            24: I021_155(self),
            26: I021_160(self),
            28: I021_077(self),
            29: I021_170(self),
            30: I021_020(self),
            32: I021_146(self),
            35: I021_016(self),
            36: I021_008(self),
            37: I021_271(self),
            38: I021_132(self),
            41: I021_400(self),
            42: I021_295(self),
            48: I021_RE(self),
        }
        return data_item_map.get(self.FRN)
        
        
    def retrieve_datalist(self):
        return self.data_list
    def retrieve_data(self):
        return self.dataitem.data
    