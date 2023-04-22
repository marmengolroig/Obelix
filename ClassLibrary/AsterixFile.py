# A class "AsterixFile" is declared with its attributes: 
# PATH - indicates the path of the file,
# DATABLOCK_LIST - is a list of DataBlock objects.

from ClassLibrary.DataBlock import DataBlock
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
                datablock = DataBlock(self.decimal_list[i]) # cat
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
    def decode_dataitems(self):
        self.datablock_list[0].decode_record()
    #    for datablock in self.datablock_list:
    #        datablock.record.decode_dataitems()
