class ShotPlacement:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def covers(self, row, col):     
        if self.col != col and self.row != row:
            return False
        return self.row == row and self.col == col

    def __repr__(self):
        if self.col == 0:
            if self.col == 0 and self.row == 0:
                self.col = 1
                self.row = 1
            self.col = 1
        if self.col > 11:
            if self.col > 11 and self.row > 11:
                self.col = 10
                self.row = 10
            self.col = 10
        if self.row == 0:
            if self.col == 0 and self.row == 0:
                self.col = 1
                self.row = 1
            self.row = 1
        if self.row > 11:
            if self.col > 11 and self.row > 11:
                self.col = 10
                self.row = 10
            self.row = 10
        return f"ShotPlacement(row={self.row}, col={self.col})"
