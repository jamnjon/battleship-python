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
    existing_ship_positions += ["carrier"] + carrier
    battleship = place_ship(existing_ship_positions, 4)
    existing_ship_positions += ["battleship"] + battleship
    submarine = place_ship(existing_ship_positions, 3)
    existing_ship_positions += ["submarine"] + submarine
    cruiser = place_ship(existing_ship_positions, 3)
    existing_ship_positions += ["cruiser"] + cruiser
    destroyer = place_ship(existing_ship_positions, 2)
    existing_ship_positions += ["destroyer"] + destroyer

    print carrier
    print battleship
    print submarine
    print cruiser
    print destroyer

    print "\n\n\n"

    return existing_ship_positions

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
                    current_ship.append(str(chr(64+start_row)) + str(coord))
                    if current_ship[-1] in existing_positions:
                        invalid_position = True
            else:
                invalid_position = True

        #ship is vertical
        else:
            if start_row < 7:
                for coord in range(start_row, start_row + ship_size):
                    current_ship.append(str(chr(64+coord)) + str(start_col))
                    if current_ship[-1] in existing_positions:
                        invalid_position = True
            else:
                invalid_position = True
    return current_ship

def take_turn(ships, hits):
    print_board(board)
    user_input =  raw_input("\n\nInput Coordinates (format is letter number, ie 'b3'):")

    # elif len(user_input) == 3 and ord(user_input[0].upper()) < 75 and ord(user_input[0].upper()) > 64 and \
    # user_input and ord(user_input[1]) < 58 and ord(user_input[2]) == 47:

    if ((len(user_input) == 2 and ord(user_input[1]) < 58 and ord(user_input[1]) > 48) or \
    (len(user_input) == 3 and user_input[1] == "1" and user_input[2] == '0')) and \
    ord(user_input[0].upper()) < 75 and ord(user_input[0].upper()) > 64:
        current_row = ord(user_input[0].upper()) - 64
        current_col = int(user_input[1])
        if len(user_input) == 3:
            current_col = 10
        # print user_input[0].upper() + user_input[1]
        if (user_input[0].upper() + str(current_col)) in ships:
            board[current_row][current_col] = u"\033[1;32;40m\u2713\033[1;37;40m"
            idx = ships.index(user_input[0].upper() + str(current_col))
            os.system("clear")

            if idx < 7:
                hits[0] -= 1
                if hits[0] == 0:
                    print "\033[1;31;40mYou Sank My Carrier!\033[1;37;40m"
            elif idx < 12:
                hits[1] -= 1
                if hits[1] == 0:
                    print "\033[1;31;40mYou Sank My Battleship!\033[1;37;40m"
            elif idx < 16:
                hits[2] -= 1
                if hits[2] == 0:
                    print "\033[1;31;40mYou Sank My Submarine!\033[1;37;40m"
            elif idx < 20:
                hits[3] -= 1
                if hits[3] == 0:
                    print "\033[1;31;40mYou Sank My Cruiser!\033[1;37;40m"
            elif idx < 23:
                hits[4] -= 1
                if hits[4] == 0:
                    print "\033[1;31;40mYou Sank My Destroyer!\033[1;37;40m"
            hits[5] -= 1
        else:
            os.system("clear")
            board[current_row][current_col] = "\033[1;31;40mX\033[1;37;40m"
    else:
        os.system("clear")

def game():
    ships = place_ships()
    hits = [5,4,3,3,2,17]
    os.system("clear")
    print "Welcome to Single Player Battleship. Guess grid spots to sink the opponent's ships."
    while hits[5]:
        take_turn(ships, hits)
    print_board(board)

game()
