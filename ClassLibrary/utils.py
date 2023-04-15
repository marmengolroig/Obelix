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