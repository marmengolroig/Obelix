# [OBELIX]

# README of the file "asterix_cat10":
# Contains 12 blocks of Asterix category 10 data. 
# Each block has one record.
# All records refer to a single moving target.

path = (
    'Ficheros_asterix/asterix_cat10', 
    'Ficheros_asterix/201002-lebl-080001_adsb.ast', 
    'Ficheros_asterix/201002-lebl-080001_mlat.ast',
    'Ficheros_asterix/201002-lebl-080001_smr.ast',
    'Ficheros_asterix/201002-lebl-080001_smr_mlat_adsb.ast')

decimal_list  = []
binary_list = []
binary_mod_list = []
byte_list = []

# A class "data_block" is declared with its specifications: CAT (1 octet) indicates the Category of the data block, LEN (2 octets) 
# indicates the number of octets of the data block (including CAT and LEN), and REC is the surveillance data of the data block.
class data_block:
    def __init__(self,CAT,LEN,REC):
        self.CAT = CAT
        self.LEN = LEN
        self.REC = []

def main():

    # open file in binary mode
    with open(path[0], "rb") as f:
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
        binary_value = bin(decimal_value) # bin() returns the binary value of a decimal
        binary_value_mod = bin(decimal_value)[2:].zfill(8)
        binary_list.append(binary_value)
        binary_mod_list.append(binary_value_mod)
        
    # print(byte_list)    
    print(decimal_list)
    # print(binary_list)
    # print(binary_mod_list)
    i=0
    new_db=True
    sum=0
    data_block_list=[]
    while i<len(decimal_list):
        if new_db:
            CAT=decimal_list[i]
            LEN=decimal_list[i+1]+decimal_list[i+2]
            REC=[]
            sum=sum+LEN
            k=0
            l=i
            while k<LEN-3:
                REC.append(data_block_list[l])
                l=l+1
                k=k+1
            
            db = data_block(CAT,LEN,REC)
            new_db=False
            data_block_list.append(db)
        if i==sum-1:
            new_db=True
        i=i+1

    print("Data blocks: "+str(len(data_block_list)))
    m = 0
    while m<len(data_block_list):
        print(data_block_list[m].CAT)
        m=m+1
    print(len(decimal_list))


if __name__ == '__main__':
    main()
