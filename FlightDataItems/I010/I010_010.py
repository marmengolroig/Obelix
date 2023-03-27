# Data Source Identifier (DSI) - I010/010
# Fixed length: 2 octets

from ClassLibrary.AsterixFile import DataItem

class I010_010(DataItem):

    def __init__(self, FRN, starting_octet):
        super().__init__(FRN, starting_octet)
        self.ref_no = 'I010/010'
        self.long = 2
        self.length_type = 0
        self.dataitem = self
        self.data = []

    """ Data Source Identifier (DSI) """

    def __init__(self):
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