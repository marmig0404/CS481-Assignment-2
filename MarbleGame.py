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
import itertools  # probably could get away without itertools


# visualize function:
#   Creates a visual representation of a marble solitaire board.
#   Takes an input of a 2D array or strings with a triangular structure.
#   See example use in __main__

def visualize(board):
    rowCount = len(board)
    for r in range(rowCount):
        output = ""
        for margin in itertools.repeat("  ", rowCount - r):  # add margins
            output += margin
        for i in range(len(board[r])):
            output += board[r][i] + "  "  # Add marble or gap
        print(output)  # Print row
    print("")


# __main__ function:
#   Example usage of the visualize function.

if __name__ == '__main__':
    MARBLE = 'O'
    GAP = '_'

    gameBoard = [
        [MARBLE],
        [MARBLE, MARBLE],
        [MARBLE, GAP, MARBLE],
        [MARBLE, MARBLE, MARBLE, MARBLE],
        [MARBLE, MARBLE, MARBLE, MARBLE, MARBLE],
    ]
    visualize(gameBoard)
