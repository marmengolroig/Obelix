# A class "Record" is declared with its attributes:
# FSPEC - is a list of binary strings, each string represents a Field Specification (FSPEC) octet,
# DATAFIELD_LIST - is a list of decimal values, each value represents a Data Field (DF) octet. 

from ClassLibrary.utils import *
from ClassLibrary.DataItemCat10 import DataItemCat10
from ClassLibrary.DataItemCat21 import DataItemCat21


class Record:
    def __init__(self):
        self.fspec = ''
        self.datafield_list = []
        self.record_decimal_list = []
        self.dataitems_list = []

    def __str__(self) -> str:
        return self.fspec + str(self.datafield_list)

    def append(self,decimal): # append decimal to record (fspec or datafield)
        self.record_decimal_list.append(decimal)
    
    def retrieve_num_datafields(self):
        return len(self.datafield_list)
    
    def divide_record(self):
        i=0
        while True:
            bin_str = decimal_to_bin_str(self.record_decimal_list[i]) # to binary
            self.fspec = self.fspec + bin_str # append binary string to fspec
            if bin_str[-1] == '0':
                break # end of fspec
            i+=1
        self.datafield_list = self.record_decimal_list[i+1:] # datafields are the rest of the record
        return (self.fspec,self.datafield_list)

    def retrieve_num_datafields(self):
        return len(self.datafield_list)
    
    def retrieve_fspec_length(self):
        return len(self.fspec)

    def retrieve_num_ones_fspec(self):
        return self.fspec.count('1')
    
    def decode_cat10(self):
        self.fspec = remove_char_in_positions(self.fspec,8) # remove FX, every 8th char
        indexes = find_indexes_of_wanted_bit(self.fspec,'1') # find indexes of 1s
        starting_octet = 0
        sum = 0
        for i,value in enumerate(self.fspec):
            if i in indexes:
                dataitem = DataItemCat10(i+1, self.datafield_list[starting_octet:]) # create dataitem
                self.dataitems_list.append(dataitem)
                starting_octet = starting_octet + dataitem.retrieve_long()
                sum +=1
                if sum == 1:
                    break
        return self.dataitems_list
    
    def decode_cat21(self):
        self.fspec = remove_char_in_positions(self.fspec,8) # remove FX, every 8th char
        indexes = find_indexes_of_wanted_bit(self.fspec,'1') # find indexes of 1s
        starting_octet = 0
        sum = 0
        for i,value in enumerate(self.fspec):
            if i in indexes:
                dataitem = DataItemCat21(i+1, self.datafield_list[starting_octet:]) # create dataitem
                self.dataitems_list.append(dataitem)
                starting_octet = starting_octet + dataitem.retrieve_long()
                sum +=1
                if sum == 17:
                    break
        return self.dataitems_list