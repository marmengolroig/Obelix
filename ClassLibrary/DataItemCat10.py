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
from FlightDataItems.I010.I010_210 import I010_210
from FlightDataItems.I010.I010_041 import I010_041
from FlightDataItems.I010.I010_220 import I010_220
from FlightDataItems.I010.I010_060 import I010_060
from FlightDataItems.I010.I010_090 import I010_090
from FlightDataItems.I010.I010_245 import I010_245
from FlightDataItems.I010.I010_300 import I010_300
from FlightDataItems.I010.I010_091 import I010_091
from FlightDataItems.I010.I010_550 import I010_550
from FlightDataItems.I010.I010_310 import I010_310
from FlightDataItems.I010.I010_500 import I010_500
from FlightDataItems.I010.I010_131 import I010_131
from FlightDataItems.I010.I010_280 import I010_280
from FlightDataItems.I010.I010_250 import I010_250


class DataItemCat10:
    def __init__(self, FRN, data_list):
        self.ref_no = ''
        self.FRN = FRN
        self.long = 0
        self.length_type = 0
        self.data_list = data_list
        self.dataitem = self.create_dataitem()
    
    def retrieve_long(self):
        return self.long

    def create_dataitem(self):
        data_item_classes = {
            1: I010_010,
            2: I010_000,
            3: I010_020,
            4: I010_140,
            5: I010_041,
            6: I010_040,
            7: I010_042,
            8: I010_200,
            9: I010_202,
            10: I010_161,
            11: I010_170,
            12: I010_060,
            13: I010_220,
            14: I010_245,
            15: I010_250,
            16: I010_300,
            17: I010_090,
            18: I010_091,
            19: I010_270,
            20: I010_550,
            21: I010_310,
            22: I010_500,
            23: I010_280,
            24: I010_131,
            25: I010_210
        }
        data_item_class = data_item_classes.get(self.FRN)
        if data_item_class:
            return data_item_class(self)
        
    def retrieve_datalist(self):
        return self.data_list
    
    def retrieve_data(self):
        return self.dataitem.data
    