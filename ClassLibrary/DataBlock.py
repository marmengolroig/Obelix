# A class "DataBlock" is declared with its attributes: 
# CAT (1 octet) - indicates the Category of the data block, 
# LONG (2 octets) - indicates the number of octets of the data block (including CAT and LONG), and 
# RECORD - is the surveillance data of the data block. 

from ClassLibrary.Record import Record
from ClassLibrary.utils import decimal_to_bin_str

class DataBlock:
    def __init__(self, cat):
        self.cat = cat
        self.long = 0
        self.record = Record()

    def decode_long(self, decimal_1, decimal_2):
        bin_str = decimal_to_bin_str(decimal_1) + decimal_to_bin_str(decimal_2)
        return int(bin_str, 2)
    
    def decode_record(self):
        if self.cat == 10:
            self.record.decode_cat10()
        elif self.cat == 21:
            self.record.decode_cat21()
