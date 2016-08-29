import os

def take_turn(board, ships, hits, guesses):
    user_input =  raw_input("\n\nInput Coordinates (format is letter number, ie 'b3'):")

    if ((len(user_input) == 2 and ord(user_input[1]) < 58 and ord(user_input[1]) > 48) or \
    (len(user_input) == 3 and user_input[1] == "1" and user_input[2] == '0')) and \
    ord(user_input[0].upper()) < 75 and ord(user_input[0].upper()) > 64:
        current_row = ord(user_input[0].upper()) - 64
        current_col = int(user_input[1])
        if len(user_input) == 3:
            current_col = 10
        guess = user_input[0].upper() + str(current_col)
        if guess not in guesses:
            guesses.append(guess)
            if (guess) in ships:
                board[current_row][current_col] = u"\033[1;32;40m\u2713\033[1;37;40m"
                idx = ships.index(guess)
                os.system("clear")
                print "\033[1;32;40mYou hit the ship at " + guess + "!\n\033[1;37;40m"

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
                print "\033[1;31;40mThere is no ship at " + guess + "!\n\033[1;37;40m"
        else:
            os.system("clear")
            print "\033[1;31;40mYou already guessed " + guess + "\n\033[1;37;40m"
    else:
        os.system("clear")
        print "\033[1;31;40mInvalid guess. Please use the proper format (ie: 'c7') and stay in bounds\n\033[1;37;40m"
