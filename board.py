import os
import random

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

def print_board(board):
    for row in board:
        print "     ".join(row)
        print " "

def place_ships():
    carrier, battleship, submarine, cruiser, destroyer = [], [], [], [], []
    existing_ship_positions = []
    carrier = place_ship(existing_ship_positions, 5)
    existing_ship_positions += carrier
    battleship = place_ship(existing_ship_positions, 4)
    existing_ship_positions += battleship
    submarine = place_ship(existing_ship_positions, 3)
    existing_ship_positions += submarine
    cruiser = place_ship(existing_ship_positions, 3)
    existing_ship_positions += cruiser
    destroyer = place_ship(existing_ship_positions, 2)
    existing_ship_positions += destroyer

    print carrier
    print battleship
    print submarine
    print cruiser
    print destroyer

    print "\n\n\n"

def place_ship(existing_positions, ship_size):
    invalid_position = True
    while invalid_position:
        current_ship = []
        invalid_position = False
        start_row =  random.randrange(1,11)
        start_col = random.randrange(1,11)
        
        #ship is horizontal
        direction = random.randrange(1,3)
        if direction == 1:
            if start_col < 7:
                for coord in range(start_col, start_col + ship_size):
                    current_ship.append([str(chr(64+start_row)) + str(coord)])
                    if current_ship[-1] in existing_positions:
                        invalid_position = True
            else:
                invalid_position = True

        #ship is vertical
        else:
            if start_row < 7:
                for coord in range(start_row, start_row + ship_size):
                    current_ship.append([str(chr(64+coord)) + str(start_col), "H"])
                    if current_ship[-1] in existing_positions:
                        invalid_position = True
            else:
                invalid_position = True
    return current_ship

place_ships()
# os.system("clear")
print "Welcome to Single Player Battleship. Guess grid spots to sink the opponent's ships."
print_board(board)
user_input =  raw_input("\n\nInput Coordinates (format is letter number, ie 'b3'):")

current_row = ord(user_input[0].upper()) - 64
current_col = int(user_input[1])
board[current_row][current_col] = "\033[1;31;40mX\033[1;37;40m"

os.system("clear")
print_board(board)
user_input =  raw_input("\n\nInput Coordinates (format is letter number, ie 'b3'):")

current_row = ord(user_input[0].upper()) - 64
current_col = int(user_input[1])
board[current_row][current_col] = u"\033[1;32;40m\u2713\033[1;37;40m"
os.system("clear")
print_board(board)
