import board
import human
import computer
import os

def game():
    guesses = []
    game_board = board.populate_empty_board()
    ships = board.place_ships()
    hits = [5,4,3,3,2,17]
    os.system("clear")
    print "Welcome to Single Player Battleship. Guess grid spots to sink the opponent's ships."
    player_type = (raw_input("type 'h' for human player or anything else for computer: ")).upper()
    board.print_board(game_board)
    if player_type == 'H':
        while hits[5]:
            human.take_turn(game_board, ships, hits, guesses)
            board.print_board(game_board)
    else:
        while hits[5]:
            computer.take_turn(game_board, ships, hits, guesses)
            board.print_board(game_board)
    board.print_board(game_board)
    print "\033[1;31;40mYou win! Great job! It took " + str(len(guesses)) + " turns.\n\033[1;37;40m"

game()
