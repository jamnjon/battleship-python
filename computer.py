import os
import random
import time

def take_turn(board, ships, hits, guesses, pending_hits, current_ship):
    ship_destroyed = False
    current_col = random.randrange(1,11)
    current_row = random.randrange(1,11)

    if len(current_ship) == 0 or len(pending_hits) == 0:
        guess = chr(64 + current_row) + str(current_col)
    else:
        guess = pending_hits[0]
        pending_hits.remove(pending_hits[0])
    if guess not in guesses:
        print guess
        # time.sleep(1)
        guesses.append(guess)
        if guess in ships:
            current_ship.append(guess)
            continue_target(board, guesses, current_ship, pending_hits, ships)
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
            board[current_row][current_col] = "\033[1;31;40mX\033[1;37;40m"
            os.system("clear")
    else:
        os.system("clear")
        print "\033[1;31;40mYou already guessed " + guess + "\n\033[1;37;40m"

def continue_target(board, guesses, current_ship, pending_hits, ships):
    last_letter = current_ship[-1][0]
    last_number = int(current_ship[-1][1:])
    invalid = [0,0,0,0]
    spaces = 1
    while 0 in invalid:
        if last_number + spaces > 10:
            invalid[0] = 1
        else:
            guess = last_letter + str(last_number + spaces)
            if guess not in guesses and (last_number + spaces) < 11:
                if guess in ships:
                    pending_hits.append(guess)

        if last_number - spaces < 1:
            invalid[1] = 1
        else:
            guess = last_letter + str(last_number - spaces)
            if guess not in guesses and (last_number - spaces) > 0:
                if guess in ships:
                    pending_hits.append(guess)

        if chr(spaces + ord(last_letter)) > 'J':
            invalid[2] = 1
        else:
            guess = chr(spaces + ord(last_letter)) + str(last_number)
            if guess not in guesses and ord(last_letter) < 75:
                if guess in ships:
                    pending_hits.append(guess)

        if (ord(last_letter) - spaces) < 65:
            invalid[3] = 1
        else:
            guess = chr(ord(last_letter) - spaces) + str(last_number)
            if guess not in guesses and ord(last_letter) > 64:
                if guess in ships:
                    pending_hits.append(guess)

        spaces += 1
