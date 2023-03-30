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
