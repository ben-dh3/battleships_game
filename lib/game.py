from lib.ship import Ship
from lib.ship_placement import ShipPlacement
from lib.shot_placement import ShotPlacement


class Game:
    def __init__(self, rows=10, cols=10):
        self.rows = rows
        self.cols = cols
        self.row = 0
        self.col = 0
        # player 1
        self.ships_placed = []
        self.unplaced_ships = [
            Ship(2),
            Ship(3),
            Ship(3),
            Ship(4),
            Ship(5),
        ]
        # player 2
        self.player2_ships_placed = []
        self.player2_unplaced_ships = [
            Ship(2),
            Ship(3),
            Ship(3),
            Ship(4),
            Ship(5),
        ]
        self.shots_fired = []
        self.player2_shots_fired = []

    # player 1
    def unplaced_ships(self):
        return self.unplaced_ships
    
    # player 2
    def player2_unplaced_ships(self):
        return self.player2_unplaced_ships
    
    # player 1
    def place_ship(self, length, orientation, row, col):
        # keep placing ships until unplaced ships is empty
        self.row = row
        self.col = col
        # player 1 loop
        while len(self.unplaced_ships) > 0:
        # check if length of ship is available
            if Ship(length) in self.unplaced_ships:
                self.check_within_board_boundary(row, col, length, orientation)
                # check there are no overlapping ships, if so, pick again        
                if self.check_overlap(length, orientation, self.row, self.col) == True:
                    break
                # remove ship from unplaced ships list
                self.unplaced_ships.remove(Ship(length))
            ship_placement = ShipPlacement(
                length=length,
                orientation=orientation,
                row=self.row,
                col=self.col,
            ) 
            self.ships_placed.append(ship_placement)
            break

    # player 2
    def player2_place_ship(self, length, orientation, row, col):
        # keep placing ships until unplaced ships is empty
        self.row = row
        self.col = col    
        while len(self.player2_unplaced_ships) > 0:
        # check if length of ship is available
            if Ship(length) in self.player2_unplaced_ships:
                self.check_within_board_boundary(row, col, length, orientation)
                # check there are no overlapping ships, if so, pick again        
                if self.player2_check_overlap(length, orientation, self.row, self.col) == True:
                    break
                # remove ship from unplaced ships list
                self.player2_unplaced_ships.remove(Ship(length))
            ship_placement = ShipPlacement(
                length=length,
                orientation=orientation,
                row=self.row,
                col=self.col,
            ) 
            self.player2_ships_placed.append(ship_placement)
            break

    # player 1 fire shot
    def fire_shot(self, row, col):
        self.row = row
        self.col = col  
        self.check_within_board_boundary(row, col)
        shot_placement = ShotPlacement(
                row=self.row,
                col=self.col,
            ) 
        self.shots_fired.append(shot_placement)

    # player 2 fire shot
    def player2_fire_shot(self, row, col):
        self.row = row
        self.col = col  
        self.check_within_board_boundary(row, col)
        shot_placement = ShotPlacement(
                row=self.row,
                col=self.col,
            ) 
        self.player2_shots_fired.append(shot_placement)


    def check_within_board_boundary(self,row, col, length=None, orientation=None):
        if orientation == 'horizontal':
            # ensure the ship starts within board boundary
            if col == 0:
                if col == 0 and row == 0:
                    self.col = 1
                    self.row = 1
                self.col = 1
            # ensure the ship ends within board boundary
            if col > 11-length:
                if col > 11-length and row > 11-length:
                    self.col = 11-length
                    self.row = 10
                self.col = 11-length
        if orientation == 'vertical':
            if row == 0:
                if col == 0 and row == 0:
                    self.col = 1
                    self.row = 1
                self.row = 1
            if row > 11-length:
                if col > 11-length and row > 11-length:
                    self.col = 10
                    self.row = 11-length
                self.row = 11-length

    # player 1
    def check_overlap(self, length, orientation, row, col):
        for i in range(0,length):
            if orientation == 'horizontal':
                if self.ship_at(row,col+i):
                    return True
            if orientation == 'vertical':
                if self.ship_at(row+i,col):
                    return True
                
    # player 2
    def player2_check_overlap(self, length, orientation, row, col):
        for i in range(0,length):
            if orientation == 'horizontal':
                if self.player2_ship_at(row,col+i):
                    return True
            if orientation == 'vertical':
                if self.player2_ship_at(row+i,col):
                    return True
        
    # player 1
    def ship_at(self, row, col):
        for ship_placement in self.ships_placed:
            if ship_placement.covers(row, col):
                return True
        return False
    
    # player 2
    def player2_ship_at(self, row, col):
        for ship_placement in self.player2_ships_placed:
            if ship_placement.covers(row, col):
                return True
        return False
    
    # player 1
    def shot_at(self, row, col):
        for shot_placement in self.shots_fired:
            if shot_placement.covers(row, col):
                return True
        return False
    
    # player 2
    def player2_shot_at(self, row, col):
        for shot_placement in self.player2_shots_fired:
            if shot_placement.covers(row, col):
                return True
        return False
