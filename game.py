import board
import human
import os

def game():
    guesses = []
    game_board = board.populate_empty_board()
    ships = board.place_ships()
    hits = [5,4,3,3,2,17]
    os.system("clear")
    print "Welcome to Single Player Battleship. Guess grid spots to sink the opponent's ships."
    while hits[5]:
        board.print_board(game_board)
        human.take_turn(game_board, ships, hits, guesses)
    board.print_board(game_board)
    print "\033[1;31;40mYou win! Great job!\n\033[1;37;40m"

game()
