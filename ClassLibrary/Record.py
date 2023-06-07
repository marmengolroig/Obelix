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
        self.dataitems_list = []

    def __str__(self):
        return self.fspec + str(self.datafield_list)

    def extend(self, decimal_list):
        self.datafield_list.extend(decimal_list)

    def divide_record(self):
        fspec_parts = []
        for decimal in self.datafield_list:
            bin_str = f'{decimal:08b}'
            fspec_parts.append(bin_str)
            if bin_str[-1] == '0':
                break
        self.fspec = ''.join(fspec_parts)
        self.datafield_list = self.datafield_list[len(self.fspec)//8:]
        return self.fspec, self.datafield_list

    def retrieve_num_datafields(self):
        return len(self.datafield_list)

    def retrieve_fspec_length(self):
        return len(self.fspec)

    def retrieve_num_ones_fspec(self):
        return self.fspec.count('1')

    def decode_cat10(self):
        self.fspec = self.fspec[:8]
        fspec_count = self.fspec.count('1')
        indexes = [i for i, value in enumerate(self.fspec) if value == '1']
        starting_octet = 0
        for index in indexes:
            dataitem = DataItemCat10(index + 1, self.datafield_list[starting_octet:])
            self.dataitems_list.append(dataitem)
            starting_octet += dataitem.retrieve_long()
            if len(self.datafield_list) == fspec_count:
                break

    def decode_cat21(self):
        self.fspec = self.fspec[:8]
        fspec_count = self.fspec.count('1')
        indexes = [i for i, value in enumerate(self.fspec) if value == '1']
        starting_octet = 0
        for index in indexes:
            dataitem = DataItemCat21(index + 1, self.datafield_list[starting_octet:])
            self.dataitems_list.append(dataitem)
            starting_octet += dataitem.retrieve_long()
            if len(self.datafield_list) == fspec_count:
                break

        
