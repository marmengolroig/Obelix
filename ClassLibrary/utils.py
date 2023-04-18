import math
import struct

def decimal_to_bin_str(decimal):
    return bin(decimal)[2:].zfill(8)

def remove_char_in_positions(string,multiple):
    new_string = ""
    for i, char in enumerate(string):
        if (i + 1) % multiple != 0:  # Check if the position is a multiple of 8
            new_string += char
    return new_string

def find_indexes_of_wanted_bit(string,bit):
    indices = []
    for i, char in enumerate(string):
        if char == bit:
            indices.append(i)
    return indices

def read_as_decimal_from_bottom(bin_str):
    return int(bin_str[::-1], 2)

def sec_to_hourminsec(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 3600) % 60
    return (hours, minutes, seconds)

def concatenate_decimals_in_binary(decimal_list):
    # convert each decimal number to 8-digit binary number
    binary_list = [format(num, '08b') for num in decimal_list]
    # concatenate the binary numbers
    concatenated_binary = ''.join(binary_list)
    return concatenated_binary

def read_in_twos_complement(binary):
        # Check if the number is negative (sign bit is 1)
    if binary[0] == '1':
        # Perform two's complement conversion
        inverted_bits = ''.join('1' if bit == '0' else '0' for bit in binary)
        decimal_number = -(int(inverted_bits, 2) + 1)
    else:
        decimal_number = int(binary, 2)
    return decimal_number

def read_character(binary):
    if binary == '000001':
        char = 'A'
    elif binary == '000010':
        char = 'B'
    elif binary == '000011':
        char = 'C'
    elif binary == '000100':
        char = 'D'
    elif binary == '000101':
        char = 'E'
    elif binary == '000110':
        char = 'F'
    elif binary == '000111':
        char = 'G'
    elif binary == '001000':
        char = 'H'
    elif binary == '001001':
        char = 'I'
    elif binary == '001010':
        char = 'J'
    elif binary == '001011':
        char = 'K'
    elif binary == '001100':
        char = 'L'
    elif binary == '001101':
        char = 'M'
    elif binary == '001110':
        char = 'N'
    elif binary == '001111':
        char = 'O'
    elif binary == '010000':
        char = 'P'
    elif binary == '010001':
        char = 'Q'
    elif binary == '010010':
        char = 'R'
    elif binary == '010011':
        char = 'S'
    elif binary == '010100':
        char = 'T'
    elif binary == '010101':
        char = 'U'
    elif binary == '010110':
        char = 'V'
    elif binary == '010111':
        char = 'W'
    elif binary == '011000':
        char = 'X'
    elif binary == '011001':
        char = 'Y'
    elif binary == '011010':
        char = 'Z'

    elif binary == '100000':
        char = ' '

    elif binary == '110000':
        char = '0'
    elif binary == '110001':
        char = '1'
    elif binary == '110010':
        char = '2'
    elif binary == '110011':
        char = '3'
    elif binary == '110100':
        char = '4'
    elif binary == '110101':
        char = '5'
    elif binary == '110110':
        char = '6'
    elif binary == '110111':
        char = '7'
    elif binary == '111000':
        char = '8'
    elif binary == '111001':
        char = '9'
    else:
        char = ''

    return(char)
