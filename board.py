import random

def populate_empty_board():
    board = []
    for row in range(11):
        board.append([])
        if row > 0:
                board[row].append(chr(64+row))
        else:
                board[row].append(" ")
        for column in range(1,11):
                if row > 0:
                        board[row].append('*')
                else:
                    board[row].append(str(column))
    return board

def print_board(board):
    for row in board:
        print "     ".join(row)
        print " "

def place_ships():
    carrier, battleship, submarine, cruiser, destroyer = [], [], [], [], []
    existing_ship_positions = []
    carrier = place_ship(existing_ship_positions, 5)
    existing_ship_positions += ["carrier"] + carrier
    battleship = place_ship(existing_ship_positions, 4)
    existing_ship_positions += ["battleship"] + battleship
    submarine = place_ship(existing_ship_positions, 3)
    existing_ship_positions += ["submarine"] + submarine
    cruiser = place_ship(existing_ship_positions, 3)
    existing_ship_positions += ["cruiser"] + cruiser
    destroyer = place_ship(existing_ship_positions, 2)
    existing_ship_positions += ["destroyer"] + destroyer

    return existing_ship_positions

def place_ship(existing_positions, ship_size):
    invalid_position = True
    while invalid_position:
        current_ship = []
        invalid_position = False
        start_row =  random.randrange(1,11)
        start_col = random.randrange(1,11)
        direction = random.randrange(1,3)

        #ship is horizontal
        if direction == 1:
            if start_col < 12 - ship_size:
                for coord in range(start_col, start_col + ship_size):
                    current_ship.append(str(chr(64+start_row)) + str(coord))
                    if current_ship[-1] in existing_positions:
                        invalid_position = True
            else:
                invalid_position = True

        #ship is vertical
        else:
            if start_row < 12 - ship_size:
                for coord in range(start_row, start_row + ship_size):
                    current_ship.append(str(chr(64+coord)) + str(start_col))
                    if current_ship[-1] in existing_positions:
                        invalid_position = True
            else:
                invalid_position = True
    return current_ship
