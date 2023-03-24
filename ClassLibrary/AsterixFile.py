from utils import *

# A class "Record" is declared with its attributes:
# FSPEC - is a list of binary strings, each string represents a Field Specification (FSPEC) octet,
# DATAFIELD_LIST - is a list of decimal values, each value represents a Data Field (DF) octet. 
class Record:
    def __init__(self):
        self.fspec = ''
        self.datafield_list = []
        self.record_decimal_list = []

    def __str__(self) -> str:
        return str(self.fspec) + str(self.datafield_list)

    def append(self,decimal): # append decimal to record (fspec or datafield)
        self.record_decimal_list.append(decimal)
    
    def retrieve_num_datafields(self):
        return len(self.datafield_list)
    
    def divide_record(self):
        i=0
        while True:
            bin_str = decimal_to_bin_str(self.record_decimal_list[i]) # to binary
            self.fspec = self.fspec + bin_str # append binary string to fspec
            if bin_str[0] == '0':
                self.fspec = self.fspec + bin_str # append binary string to fspec
                break # end of fspec
            i+=1
        bin_str = decimal_to_bin_str(self.record_decimal_list[i+1]) # to binary
        self.fspec = self.fspec + bin_str # append binary string to fspec
        self.datafield_list = self.record_decimal_list[i+9:] # datafields are the rest of the record

    def retrieve_num_datafields(self):
        return len(self.datafield_list)
    
    def retrieve_fspec_length(self):
        return len(self.fspec)

# A class "DataBlock" is declared with its attributes: 
# CAT (1 octet) - indicates the Category of the data block, 
# LONG (2 octets) - indicates the number of octets of the data block (including CAT and LONG), and 
# RECORD - is the surveillance data of the data block. 
class DataBlock:
    def __init__(self,cat):
        self.cat = cat
        self.long = 0
        self.record = Record()

    def decode_long(self,decimal_1,decimal_2):
        bin_str = decimal_to_bin_str(decimal_1) + decimal_to_bin_str(decimal_2) 
        return int(bin_str,2)

# A class "AsterixFile" is declared with its attributes: 
# PATH - indicates the path of the file,
# DATABLOCK_LIST - is a list of DataBlock objects.
class AsterixFile:
    def __init__(self, path):
        self.path = path
        self.datablock_list = []
        self.decimal_list = []

    def retrieve_num_datablocks(self):
        return len(self.datablock_list)

    def read_file(self):
        self.decimal_list  = []
        byte_list = []
        # open file in binary mode
        with open(self.path, "rb") as f:
            while True: # read byte by byte
                byte = f.read(1) # read 1 byte
                if not byte: 
                    break # end of file
                byte_list.append(byte)
        
        for byte in byte_list:
            # to decimal
            decimal_value = ord(byte) # ord() returns the integer value of a byte
            self.decimal_list.append(decimal_value)

        return self.decimal_list
    
    def divide_datablocks(self):
        i=0
        new_datablock=True
        sum=0
        n=0
        while i < len(self.decimal_list):
            if new_datablock:   
                datablock = DataBlock(self.decimal_list[i]) # long is 0 because it will be calculated later
                datablock.long = datablock.decode_long(self.decimal_list[i+1],self.decimal_list[i+2]) # calculate long
                self.datablock_list.append(datablock) # add datablock to datablock_list

                sum=sum+datablock.long
                l=i+3 # l is the index of the first decimal of the record

                while l<i+datablock.long:
                    self.datablock_list[n].record.append(self.decimal_list[l]) # add decimal to record
                    l=l+1
                new_datablock=False # next decimal
                n=n+1 # next datablock
            if i==sum-1:
                new_datablock=True # next datablock
            i=i+1 # next decimal
        return self.datablock_list
    def divide_records(self):
        for datablock in self.datablock_list:
            datablock.record.divide_record()