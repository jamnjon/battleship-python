import board
import human
import computer
import os
import time

def game():
    guesses = []
    pending_hits = []
    game_board = board.populate_empty_board()
    ships = board.place_ships()
    hits = [5,4,3,3,2,17]
    os.system("clear")
    print "Welcome to Single Player Battleship. Guess grid spots to sink the opponent's ships."
    player_type = (raw_input("input 'c' for incomplete computer player or anything else for human: ")).upper()
    if player_type == 'C':
        while hits[5]:
            board.print_board(game_board)
            computer.take_turn(game_board, ships, hits, guesses, pending_hits, current_ship)
            # time.sleep(1)
    else:
        current_ship = []
        while hits[5]:
            board.print_board(game_board)
            human.take_turn(game_board, ships, hits, guesses)
    board.print_board(game_board)
    print ships
    print guesses
    print "\033[1;31;40mYou win! Great job! It took " + str(len(guesses)) + " turns.\n\033[1;37;40m"

game()
