# Message Type (MT) - (I010/000)
# Fixed length: 1 octet


class I010_000():

    def __init__(self, parent):
        self.parent = parent
        self.parent.ref_no = 'I010/000'
        self.parent.long = self.set_long()
        self.parent.length_type = 0 # 0: fixed, 1: extended, 2: repetitive, 3: compound
        self.parent.dataitem = self
        self.data = self.set_data()
        self.MT = 0

    def set_long(self):
        return 1
    
    def set_data(self):
        return self.parent.data_list[0:self.parent.long]
