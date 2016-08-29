# Battle Ship

Battle Ship is a console based python game based off the classic board game. You pick coordinates in an effort to sink all of your opponents ships. Once you sink all 5 ships, you win!

![gameplay](https://github.com/jamnjon/battleship-python/blob/master/gameplay.png)

## Implementation

The board is configured as a 10 x 10 grid, the pieces are placed utilizing the `random` module. The player then sees the empty grid and is able to make guesses as to the location of the ships. If the player hits a ship a green checkmark is displayed, and if they miss a red 'x'. Once the player sinks all five ships, they win.  This was my very first foray into Python, so a large portion of this was figuring out the differences between Python and other programming languages I have worked with.

Logic for placing a horizontal piece (after randomly generating a position), ensuring the ship does not overlap with any others and remains within the boundaries of the board.
````python
if direction == 1:
  if start_col < 12 - ship_size:
    for coord in range(start_col, start_col + ship_size):
      current_ship.append(str(chr(64+start_row)) + str(coord))
      if current_ship[-1] in existing_positions:
        invalid_position = True
      else:
        invalid_position = True
````

### Future Plans

I intend to complete the AI for the computer player, allow the human player to play against them, and allow the user to place their own ships. As of right now, the AI merely picks a location at random until it hits a ship, and then checks to the right, the left, ... The flaw in this is that, as it stands now, if I pick a piece in the middle, it will check to the right, but it will not backtrack to the left after the fact. Once it runs out of connected pieces, it goes back to random selection. I have a couple of ideas that I intend to work with to fix this bug.
