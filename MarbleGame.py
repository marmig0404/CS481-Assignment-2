###
# visualize.py
#
# Martin Miglio
# CS481 - Assignment 2
# Kettering University
#
# Usage:
# Import 'from MarbleGame import visualize', or
# run 'python ./MarbleGame.py' for example
###


# imports
from itertools import repeat # probably could get away without itertools


# visualize function:
#   Creates a visual representation of a marble solitaire board.
#   Takes an input of a 2D array or strings with a triangular structure.
#   See example use in __main__

def visualize(game_board):
    row_count = len(game_board)
    for row_index in range(row_count):
        # Add margins
        output = "".join(repeat("  ", row_count - row_index))
        # Add marble or gap
        for column_index in range(len(game_board[row_index])):
            output += game_board[row_index][column_index] + "  "
        print(output)  # Print row
    print("")


# changeArrayShape function:
#   Changes shape of array from one dimensional (positions 0-14)
#   to a triangular array for printing.

def changeArrayShape(board_in_line):
    triangular_board = []
    num_of_rows = 5
    board_in_line_index = 0 
    for row_index in range(num_of_rows + 1):
        row = []
        for _ in range(row_index):
            row.append(board_in_line[board_in_line_index])
            board_in_line_index += 1
        triangular_board.append(row)
    return triangular_board

# __main__ function:
#   Example usage of the visualize function.
if __name__ == '__main__':
    MARBLE = 'O'
    GAP = '_'

    # Using triangular array
    game_board = [
        [MARBLE],
        [MARBLE, MARBLE],
        [MARBLE, GAP, MARBLE],
        [MARBLE, MARBLE, MARBLE, MARBLE],
        [MARBLE, MARBLE, MARBLE, MARBLE, MARBLE],
    ]
    visualize(game_board)

    # Using single row array
    game_board = [MARBLE, MARBLE, MARBLE, MARBLE, GAP, MARBLE, MARBLE,
                 MARBLE, MARBLE, MARBLE, MARBLE, MARBLE, MARBLE, MARBLE, MARBLE]
    visualize(changeArrayShape(game_board))
