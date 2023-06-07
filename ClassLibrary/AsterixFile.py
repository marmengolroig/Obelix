# A class "AsterixFile" is declared with its attributes: 
# PATH - indicates the path of the file,
# DATABLOCK_LIST - is a list of DataBlock objects.

from ClassLibrary.DataBlock import DataBlock
class AsterixFile:
    def __init__(self, path):
        self.path = path
        self.datablock_list = []

    def retrieve_num_datablocks(self):
        return len(self.datablock_list)

    def read_file(self):
        with open(self.path, "rb") as f:
            self.decimal_list = bytearray(f.read())
        return self.decimal_list

    def divide_datablocks(self):
        i = 0
        new_datablock = True
        n = 0
        sum_value = 0
        while i < len(self.decimal_list):
            if new_datablock:
                cat = self.decimal_list[i]
                datablock = DataBlock(cat)
                datablock.long = datablock.decode_long(self.decimal_list[i+1], self.decimal_list[i+2])
                self.datablock_list.append(datablock)
                sum_value += datablock.long
                l = i + 3
                datablock.record.extend(self.decimal_list[l:l+datablock.long])
                new_datablock = False
                n += 1
            if i == sum_value - 1:
                new_datablock = True
            i += 1
        return self.datablock_list

    def decode_dataitems(self):
        for datablock in self.datablock_list:
            datablock.record.divide_record()
            datablock.decode_record()
