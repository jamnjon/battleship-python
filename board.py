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

user_input = "b3"
current_row = ord(user_input[0].upper()) - 64
current_col = int(user_input[1])
board[current_row][current_col] = "\033[1;31;40mX\033[1;37;40m"
user_input = "c4"
current_row = ord(user_input[0].upper()) - 64
current_col = int(user_input[1])
board[current_row][current_col] = u"\033[1;32;40m\u2713\033[1;37;40m"
print_board(board)
