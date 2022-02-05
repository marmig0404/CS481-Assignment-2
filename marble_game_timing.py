"""
# visualize.py
#
# Martin Miglio
# CS481 - Assignment 2
# Kettering University
#
# Usage:
# run 'python ./marble_game_timing.py'
"""

import time
import numpy as np
from marble_game import breadth_first_search, visualize


def change_array_shape(board_in_line):
    """
    # change_array_shape function:
    #   changes a 1D array into a tiangular 2D array
    """

    triangular_board = []
    num_of_rows = 5
    board_in_line_index = 0
    for row_index in range(num_of_rows + 1):
        row = []
        for _ in range(row_index):
            row.append(board_in_line[board_in_line_index])
            board_in_line_index += 1
        triangular_board.append(row)
    return [x for x in triangular_board if x != []]


def round_board(board):
    """
    # round_board function:
    #   rounds values in a board to 0 or 1
    """

    return np.where(board <= 0.5, 0, 1)


def stress_test_random(number_of_boards, board_length):
    """
    # stress_test_random function:
    #   generates random starting boards to test
    """

    return list(map(round_board, np.random.rand(number_of_boards, board_length)))


def stress_test_normal(number_of_boards, board_length):
    """
    # stress_test_normal function:
    #   generates standard starting boards to test (one marble missing)
    """

    boards = np.ones((number_of_boards, board_length), int)
    np.fill_diagonal(boards, 0)
    return list(boards)


if __name__ == '__main__':
    # Strings to represent positions
    MARBLE = 'O'
    GAP = '_'

    NUMBER_OF_BOARDS = 10
    BOARD_LENGTH = 15

    STARTING_BOARDS = stress_test_random(NUMBER_OF_BOARDS, BOARD_LENGTH)
    #STARTING_BOARDS = stress_test_normal(NUMER_OF_BOARDS, BOARD_LENGTH)

    print(STARTING_BOARDS)
    STARTING_BOARDS = list(map(change_array_shape, STARTING_BOARDS))

    DURATIONS = []
    for game_board_index, game_board  in enumerate(STARTING_BOARDS):
        start = time.time()
        print(f"--- Starting board {game_board_index + 1}/{len(STARTING_BOARDS)}: ---")
        visualize(game_board, MARBLE, GAP)
        visualize(breadth_first_search(
            game_board, print_count=True, track_memory=True, verbose=False), MARBLE, GAP)
        duration = time.time() - start
        print(f'-- Took {duration:.2f} s to find solution. --')
        DURATIONS.append(duration)
    print(
        f'--- Average time to complete {(sum(DURATIONS)/len(DURATIONS)):.2f} s ---')
