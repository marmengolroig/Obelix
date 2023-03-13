# [OBELIX] - [python]

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
byte_list = []

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
        binary_list.append(binary_value)
        
    print(byte_list)    
    print(decimal_list)
    print(binary_list)

if __name__ == '__main__':
    main()