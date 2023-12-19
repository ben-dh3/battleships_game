class UserInterface:
    def __init__(self, io, game):
        self.io = io
        self.game = game
        self.p1_points = 0
        self.p2_points = 0

    def run(self):
        self._show("Welcome to the game!")
        self._show("Set up your ships first.")
        # player 1: run until unplaced_ships is empty
        while len(self.game.unplaced_ships) > 0:
            self._show("PLAYER 1 PICK - player 2, look away")
            self._show("You have these ships remaining: {}".format(
                self._ships_unplaced_message()))
            self._prompt_for_ship_placement()
            self._show("This is your board now:")
            self._show(self._format_board())
            self._show("Done, for now!")
        # player 2:
        while len(self.game.player2_unplaced_ships) > 0:
            self._show("PLAYER 2 PICK - player 1, look away")
            self._show("You have these ships remaining: {}".format(
                self._player2_ships_unplaced_message()))
            self._player2_prompt_for_ship_placement()
            self._show("This is your board now:")
            self._show(self._player2_format_board())
            self._show("Done, for now!")
        # attack phase
        # while both boards have not got 17 hits - play round
        while self.p1_points != 17 and self.p2_points != 17:
            self._show("PLAYER 1 - choose where to fire")
            self._show(self._hidden_board())
            self._prompt_for_shot_placement()
            self._show(self._hidden_board())
            self._show("PLAYER 2 - choose where to fire")
            self._show(self._player2_hidden_board())
            self._player2_prompt_for_shot_placement()
            self._show(self._player2_hidden_board())
        if self.p1_points == 17:
            self._show("PLAYER 1 WINS")
        if self.p2_points == 17:
            self._show("PLAYER 2 WINS")

    def _show(self, message):
        self.io.write(message + "\n")

    def _prompt(self, message):
        self.io.write(message + "\n")
        return self.io.readline().strip()

    # player 1
    def _ships_unplaced_message(self):
        ship_lengths = [str(ship.length) for ship in self.game.unplaced_ships]
        return ", ".join(ship_lengths)
    
    # player 2
    def _player2_ships_unplaced_message(self):
        ship_lengths = [str(ship.length) for ship in self.game.player2_unplaced_ships]
        return ", ".join(ship_lengths)
    
    # player 1
    def _prompt_for_ship_placement(self):
        ship_length = self._prompt("Which do you wish to place?")
        ship_orientation = self._prompt("Vertical or horizontal? [vh]")
        ship_row = self._prompt("Which row?")
        ship_col = self._prompt("Which column?")
        self._show("OK.")
        self.game.place_ship(
            length=int(ship_length),
            orientation={"v": "vertical", "h": "horizontal"}[ship_orientation],
            row=int(ship_row),
            col=int(ship_col),
        )

    # player 2
    def _player2_prompt_for_ship_placement(self):
        ship_length = self._prompt("Which do you wish to place?")
        ship_orientation = self._prompt("Vertical or horizontal? [vh]")
        ship_row = self._prompt("Which row?")
        ship_col = self._prompt("Which column?")
        self._show("OK.")
        self.game.player2_place_ship(
            length=int(ship_length),
            orientation={"v": "vertical", "h": "horizontal"}[ship_orientation],
            row=int(ship_row),
            col=int(ship_col),
        )

    # player 1
    def _format_board(self):
        rows = []
        for row in range(1, self.game.rows + 1):
            row_cells = []
            for col in range(1, self.game.cols + 1):
                if self.game.ship_at(row, col):
                    row_cells.append("S")
                else:
                    row_cells.append(".")
            rows.append("".join(row_cells))
        return "\n".join(rows)
    
    # player 2
    def _player2_format_board(self):
        rows = []
        for row in range(1, self.game.rows + 1):
            row_cells = []
            for col in range(1, self.game.cols + 1):
                if self.game.player2_ship_at(row, col):
                    row_cells.append("S")
                else:
                    row_cells.append(".")
            rows.append("".join(row_cells))
        return "\n".join(rows)
    
    # player 1
    def _prompt_for_shot_placement(self):
        shot_row = self._prompt("Which row?")
        shot_col = self._prompt("Which column?")
        self._show("OK.")
        self.game.fire_shot(
            row=int(shot_row),
            col=int(shot_col),
        )

    # player 2
    def _player2_prompt_for_shot_placement(self):
        shot_row = self._prompt("Which row?")
        shot_col = self._prompt("Which column?")
        self._show("OK.")
        self.game.player2_fire_shot(
            row=int(shot_row),
            col=int(shot_col),
        )

    # player 1
    def _hidden_board(self):
        self.p1_points = 0
        rows = []
        for row in range(1, self.game.rows + 1):
            row_cells = []
            for col in range(1, self.game.cols + 1):
                if self.game.shot_at(row, col):
                    if self.game.player2_ship_at(row, col):
                        row_cells.append("X")
                        self.p1_points+=1
                    else:
                        row_cells.append("O")    
                else:
                    row_cells.append(".")
            rows.append("".join(row_cells))
        return "\n".join(rows)
    
    # player 2
    def _player2_hidden_board(self):
        self.p2_points = 0
        rows = []
        for row in range(1, self.game.rows + 1):
            row_cells = []
            for col in range(1, self.game.cols + 1):
                if self.game.player2_shot_at(row, col): 
                    if self.game.ship_at(row, col):
                        row_cells.append("X")
                        self.p2_points+=1
                    else:
                        row_cells.append("O")
                else:
                    row_cells.append(".")
            rows.append("".join(row_cells))
        return "\n".join(rows)

