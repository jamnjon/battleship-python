import os
import random

def take_turn(board, ships, hits, guesses):
    current_col = random.randrange(1,11)
    current_row = random.randrange(1,11)
    guess = chr(64 + current_row) + str(current_col)
    if guess not in guesses:
        guesses.append(guess)
        if (guess) in ships:
            board[current_row][current_col] = u"\033[1;32;40m\u2713\033[1;37;40m"
            idx = ships.index(guess)
            os.system("clear")

            if idx < 7:
                hits[0] -= 1
                if hits[0] == 0:
                    print "\033[1;31;40mYou Sank My Carrier!\n\033[1;37;40m"
            elif idx < 12:
                hits[1] -= 1
                if hits[1] == 0:
                    print "\033[1;31;40mYou Sank My Battleship!\n\033[1;37;40m"
            elif idx < 16:
                hits[2] -= 1
                if hits[2] == 0:
                    print "\033[1;31;40mYou Sank My Submarine!\n\033[1;37;40m"
            elif idx < 20:
                hits[3] -= 1
                if hits[3] == 0:
                    print "\033[1;31;40mYou Sank My Cruiser!\n\033[1;37;40m"
            elif idx < 23:
                hits[4] -= 1
                if hits[4] == 0:
                    print "\033[1;31;40mYou Sank My Destroyer!\n\033[1;37;40m"
            hits[5] -= 1
        else:
            os.system("clear")
            board[current_row][current_col] = "\033[1;31;40mX\033[1;37;40m"
    else:
        os.system("clear")
        print "\033[1;31;40mYou already guessed " + guess + "\n\033[1;37;40m"
