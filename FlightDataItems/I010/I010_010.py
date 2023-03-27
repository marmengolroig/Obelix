# Data Source Identifier (DSI) - I010/010
# Fixed length: 2 octets

class I010_010():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I010/010'
        self.parent.long = 2
        self.parent.length_type = 0 # 0: fixed, 1: extended, 2: repetitive, 3: compound
        self.parent.dataitem = self
        self.parent.data = []
        self.SAC = 0
        self.SIC = 0

    def set_long(self):
        self.long = 2

    def decode(self, record):
        """ Decode Data Source Identifier (DSI) field """

        # Get the first octet
        first_octet = record[0]
        # Get the second octet
        second_octet = record[1]
        # Get the first 2 bits
        first_2_bits = first_octet[0:2]
        # Get the next 6 bits
        next_6_bits = first_octet[2:8]
        # Get the next 8 bits
        next_8_bits = second_octet[0:8]
        # Get the last 8 bits
        last_8_bits = second_octet[8:16]
        # Get the first 2 bits
        first_2_bits = first_octet[0:2]
        # Get the next 6 bits
        next_6_bits = first_octet[2:8]
        # Get the next 8 bits
        next_8_bits = second_octet[0:8]
        # Get the last 8 bits
        last_8_bits = second_octet[8:16]
        # Get the first 2 bits
        first_2_bits = first_octet[0:2]
        # Get the next 6 bits
        next_6_bits = first_octet[2:8]
        # Get the next 8 bits
        next_8_bits = second_octet[0:8]
        # Get the last 8 bits
        last_8_bits = second_octet[8:16]
        # Get the first 2 bits
        first_2_bits = first_octet[0:2]
        # Get the next 6 bits
        next_6_bits = first_octet[2:8]
        # Get the next 8 bits
        next_8_bits = second_octet[0:8]
        # Get the last 8 bits
        last_8_bits = second_octet[8:16]
        # Get the first 2 bits
        first_2_bits = first_octet[0:2]
        # Get the next 6 bits
        next_6_bits = first_octet[2:8]