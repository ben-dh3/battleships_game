class ShipPlacement:
    def __init__(self, length, orientation, row, col):
        self.length = length
        self.orientation = orientation
        self.row = row
        self.col = col

    def covers(self, row, col):
        if self.orientation == "vertical":
            if self.col != col:
                return False
            return self.row <= row < self.row + self.length
        else:
            if self.row != row:
                return False
            return self.col <= col < self.col + self.length

    def __repr__(self):
        if self.orientation == 'horizontal':
            # ensure the ship starts within board boundary
            if self.col == 0:
                if self.col == 0 and self.row == 0:
                    self.col = 1
                    self.row = 1
                self.col = 1
            # ensure the ship ends within board boundary
            if self.col > 11-self.length:
                if self.col > 11-self.length and self.row > 10:
                    self.col = 11-self.length
                    self.row = 10
                self.col = 11-self.length
        if self.orientation == 'vertical':
            if self.row == 0:
                if self.col == 0 and self.row == 0:
                    self.col = 1
                    self.row = 1
                self.row = 1
            if self.row > 11-self.length:
                if self.col > 10 and self.row > 11-self.length:
                    self.col = 10
                    self.row = 11-self.length
                self.row = 11-self.length
        return f"ShipPlacement(length={self.length}, orientation={self.orientation}, row={self.row}, col={self.col})"
