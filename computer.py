import os
import random

def take_turn(board, ships, hits, guesses, current_ship):
    ship_destroyed = False
    current_col = random.randrange(1,11)
    current_row = random.randrange(1,11)
    if len(current_ship) == 0:
        guess = chr(64 + current_row) + str(current_col)
    else:
        guess = continue_target(board, guesses, current_ship)
    if guess not in guesses:
        guesses.append(guess)
        if (guess) in ships:
            current_ship.append(guess)
            board[current_row][current_col] = u"\033[1;32;40m\u2713\033[1;37;40m"
            idx = ships.index(guess)
            os.system("clear")

            if idx < 7:
                hits[0] -= 1
                if hits[0] == 0:
                    print "\033[1;31;40mYou Sank My Carrier!\n\033[1;37;40m"
                    ship_destroyed = True
            elif idx < 12:
                hits[1] -= 1
                if hits[1] == 0:
                    print "\033[1;31;40mYou Sank My Battleship!\n\033[1;37;40m"
                    ship_destroyed = True
                    current_ship = []
            elif idx < 16:
                hits[2] -= 1
                if hits[2] == 0:
                    print "\033[1;31;40mYou Sank My Submarine!\n\033[1;37;40m"
                    ship_destroyed = True
                    current_ship = []
            elif idx < 20:
                hits[3] -= 1
                if hits[3] == 0:
                    print "\033[1;31;40mYou Sank My Cruiser!\n\033[1;37;40m"
                    ship_destroyed = True
                    current_ship = []
            elif idx < 23:
                hits[4] -= 1
                if hits[4] == 0:
                    print "\033[1;31;40mYou Sank My Destroyer!\n\033[1;37;40m"
                    ship_destroyed = True
                    current_ship = []
            hits[5] -= 1
        else:
            os.system("clear")
            board[current_row][current_col] = "\033[1;31;40mX\033[1;37;40m"
    else:
        os.system("clear")
        print "\033[1;31;40mYou already guessed " + guess + "\n\033[1;37;40m"

def continue_target(board, guesses, current_ship):
    last_letter = current_ship[-1][0]
    last_number = int(current_ship[-1][1:])
    guess = last_letter + str(last_number + 1)
    if guess not in guesses and (last_number + 1) < 11:
        return guess
    else:
        guess = last_letter + str(last_number - 1)
    if guess not in guesses and (last_number - 1) > 0:
        return guess
    else:
        guess = chr(1 + ord(last_letter)) + str(last_number)
    if guess not in guesses and ord(last_letter) < 75:
        return guess
    else:
        guess = chr(ord(last_letter) - 1) + str(last_number)
    if guess not in guesses and ord(last_letter) > 64:
        return guess
    else:
        current_ship = []
        return chr(random.randrange(1,11) + 64) + str(random.randrange(1,11))
