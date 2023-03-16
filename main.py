# [OBELIX]

# README of the file "asterix_cat10":
# Contains 12 blocks of Asterix category 10 data. 
# Each block has one record.
# All records refer to a single moving target.

path = (
    'Ficheros_asterix/asterix_cat10', 
    'Ficheros_asterix/201002-lebl-080001_adsb.ast', #cat 21
    'Ficheros_asterix/201002-lebl-080001_mlat.ast', #cat 10
    'Ficheros_asterix/201002-lebl-080001_smr.ast', #cat 10
    'Ficheros_asterix/201002-lebl-080001_smr_mlat_adsb.ast') # mixed

decimal_list  = []
binary_list = []
binary_mod_list = []
byte_list = []

# A class "data_block" is declared with its specifications: CAT (1 octet) indicates the Category of the data block, LEN (2 octets) 
# indicates the number of octets of the data block (including CAT and LEN), and REC is the surveillance data of the data block.
class data_block:
    def __init__(self,cat,len,data):
        self.cat = cat
        self.len = len
        self.data = data

def main():

    # open file in binary mode
    with open(path[4], "rb") as f:
        while True: # read byte by byte
            byte = f.read(1) # read 1 byte
            if not byte: 
                break # end of file
            byte_list.append(byte)
    
    for byte in byte_list:
        # to decimal
        decimal_value = ord(byte) # ord() returns the integer value of a byte
        decimal_list.append(decimal_value)
       

        # to binary
        # binary_value = bin(decimal_value) # bin() returns the binary value of a decimal
        # binary_value_mod = bin(decimal_value)[2:].zfill(8)
        # binary_list.append(binary_value)
        # binary_mod_list.append(binary_value_mod)
        
    # print(byte_list)    
    # print(decimal_list)
    # print(binary_list)
    # print(binary_mod_list)
    i=0
    new_db=True
    sum=0
    data_block_list=[]
    n=0
    while i<len(decimal_list):
        if new_db:
            CAT=decimal_list[i]
            bin_str=bin(decimal_list[i+1])[2:].zfill(8)+bin(decimal_list[i+2])[2:].zfill(8)
            LEN=int(bin_str,2)
            data=[]
            data_block_list.append(data_block(CAT,LEN,data))
            sum=sum+LEN
            l=i
            while l<i+LEN:
                data_block_list[n].data.append(decimal_list[l])
                l=l+1
            new_db=False
            n=n+1
        if i==sum-1:
            new_db=True
        i=i+1

    print("Data blocks: "+str(len(data_block_list)))
    m = 0
    while m<3:
        print(data_block_list[m].data)
        m=m+1


if __name__ == '__main__':
    main()
