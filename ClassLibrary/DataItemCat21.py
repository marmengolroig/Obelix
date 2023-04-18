# A class "DataItem" is declared with its attributes:
# REF_NO- is the identifier of the data item,
# LONG - is the length of the data item in octets,

from FlightDataItems.I021.I021_010 import I021_010



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
        
        
    def retrieve_datalist(self):
        return self.data_list
    def retrieve_data(self):
        return self.dataitem.data
    