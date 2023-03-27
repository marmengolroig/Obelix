# A class "Record" is declared with its attributes:
# FSPEC - is a list of binary strings, each string represents a Field Specification (FSPEC) octet,
# DATAFIELD_LIST - is a list of decimal values, each value represents a Data Field (DF) octet. 

from ClassLibrary.utils import decimal_to_bin_str
from ClassLibrary.DataItem import DataItem

class Record:
    def __init__(self):
        self.fspec = ''
        self.datafield_list = []
        self.record_decimal_list = []

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

    def retrieve_num_datafields(self):
        return len(self.datafield_list)
    
    def retrieve_fspec_length(self):
        return len(self.fspec)

    def retrieve_num_dataitems(self):
        return self.fspec.count('1')
    
    def identify_dataitems(self): # trencar la llista datafield_list en dataitems
        # mirar el index de la posicio dels 1s de fspec
        # comprovar si index+1 es multiple de 8 o no
        # si es multiple de 8, es un FX
        # si no es multiple de 8, es un Dataitem
            # llavors, s'haurà de mirar quin data item és

#########################
        FRN = 1 # CANVIAR!!
        starting_octet = 0 # CANVIAR!!
#########################
        dataitem = DataItem(FRN, starting_octet)
#         dataitem.dataitem.set_long(self.datafield_list)
#         # ja podem dividir el datafield_list en dataitems
# #########################
#         parsed_datafield_list = self.datafield_list[0:2] # CANVIAR!!
# #########################
#         dataitem.set_data(parsed_datafield_list)
        return dataitem