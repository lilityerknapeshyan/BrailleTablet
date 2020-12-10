class Tablet:
    
    def __init__(self, cell_amount_hor, cell_amount_ver):
        self.cell_amount_hor = cell_amount_hor
        self.cell_amount_ver = cell_amount_ver

    def get_char_capacity(self):
        char_capacity = self.cell_amount_ver * self.cell_amount_hor
        return char_capacity
