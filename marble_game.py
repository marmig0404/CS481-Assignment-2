"""
# visualize.py
#
# Martin Miglio
# CS481 - Assignment 2
# Kettering University
#
# Usage:
# run 'python ./marble_game.py'
"""

import copy
import sys
from itertools import repeat


def visualize(game_state, marble_icon, gap_icon):
    """
    # visualize function:
    #   Creates a visual representation of a marble solitaire board.
    #   Takes an input of a 2D binary array with a triangular structure.
    """
    if game_state is None:
        return False
    row_count = len(game_state)
    for row_index in range(row_count):
        # Add margins
        output = "".join(repeat("  ", row_count - row_index))
        # Add marble or gap
        for column_index in range(len(game_state[row_index])):
            output += (gap_icon if game_state[row_index]
                       [column_index] == 0 else marble_icon) + "  "
        print(output)  # Print row
    print("")
    return True


def find_updated_boards(game_state):
    """
    # find_updated_boards function:
    #   Finds all next possible game states given a game state.
    #   Will return empty list if no next game states are possible.
    #
    #   Details:
    #       This function is based on checking from a gap position,
    #       which marbles may jump into it. If a jump is successful,
    #       the move is considered possible and added to game states.
    #       A case classification of 'types' of jumps was developed
    #       for each position. The same 'type' of jump will involve
    #       the same calculation for finding a potential jumping marble.
    #
    #       Note: this function is complex, but I could not boil it
    #       down to a simpiler fashion, so I handled the cases explicitly.
    """

    updated_boards = []
    number_of_rows = len(game_state)
    for row_index in range(number_of_rows):  # check every row and position...
        number_of_positions = len(game_state[row_index])
        for position_index in range(number_of_positions):
            if game_state[row_index][position_index] == 0:  # if position is a gap
                gap_location = [row_index, position_index]
                # if marble can jump right...
                if gap_location in [[3, 2], [3, 3], [4, 3], [4, 4]]:

                    # from same row.
                    jumper_location = [gap_location[0], gap_location[1] - 2]
                    updated_boards.append(
                        do_jump(gap_location, jumper_location, game_state))
                    # from the row 2 above.
                    jumper_location = [
                        gap_location[0] - 2, gap_location[1] - 2]
                    updated_boards.append(
                        do_jump(gap_location, jumper_location, game_state))

                # if marble can jump down and to left...
                elif gap_location in [[3, 0], [3, 1], [4, 0], [4, 1]]:

                    # from same row.
                    jumper_location = [gap_location[0], gap_location[1] + 2]
                    updated_boards.append(
                        do_jump(gap_location, jumper_location, game_state))
                    # from the row 2 above.
                    jumper_location = [
                        gap_location[0] - 2, gap_location[1]]
                    updated_boards.append(
                        do_jump(gap_location, jumper_location, game_state))

                # if marble can jump up...
                elif gap_location in [[0, 0], [1, 0], [1, 1], [2, 1]]:

                    # from the left.
                    jumper_location = [gap_location[0] + 2, gap_location[1]]
                    updated_boards.append(
                        do_jump(gap_location, jumper_location, game_state))
                    # from the right.
                    jumper_location = [
                        gap_location[0] + 2, gap_location[1] + 2]
                    updated_boards.append(
                        do_jump(gap_location, jumper_location, game_state))

                else:  # odd cases
                    if gap_location == [2, 2]:  # if marble can jump right...

                        # from the row 2 below to the left.
                        jumper_location = [4, 2]
                        updated_boards.append(
                            do_jump(gap_location, jumper_location, game_state))
                        # from the row 2 below to the right.
                        jumper_location = [4, 4]
                        updated_boards.append(
                            do_jump(gap_location, jumper_location, game_state))
                        # from the same row.
                        jumper_location = [2, 0]
                        updated_boards.append(
                            do_jump(gap_location, jumper_location, game_state))
                        # from the row 2 above.
                        jumper_location = [0, 0]
                        updated_boards.append(
                            do_jump(gap_location, jumper_location, game_state))

                    elif gap_location == [2, 0]:  # if marble can jump left...

                        # from the row 2 below to the right.
                        jumper_location = [4, 2]
                        updated_boards.append(
                            do_jump(gap_location, jumper_location, game_state))
                        # from the row 2 below to the left.
                        jumper_location = [4, 0]
                        updated_boards.append(
                            do_jump(gap_location, jumper_location, game_state))
                        # from the same row.
                        jumper_location = [2, 2]
                        updated_boards.append(
                            do_jump(gap_location, jumper_location, game_state))
                        # from the row 2 above
                        jumper_location = [0, 0]
                        updated_boards.append(
                            do_jump(gap_location, jumper_location, game_state))

                    else:  # if marble can jump down...

                        # from the row 2 above to the left.
                        jumper_location = [2, 0]
                        updated_boards.append(
                            do_jump(gap_location, jumper_location, game_state))
                        # from the row 2 above to the right.
                        jumper_location = [2, 2]
                        updated_boards.append(
                            do_jump(gap_location, jumper_location, game_state))
                        # from the same row to the left.
                        jumper_location = [4, 0]
                        updated_boards.append(
                            do_jump(gap_location, jumper_location, game_state))
                        # from the same row to the right.
                        jumper_location = [4, 4]
                        updated_boards.append(
                            do_jump(gap_location, jumper_location, game_state))

    return list(filter(None, updated_boards))  # remove None values from list.


def do_jump(gap_location, jumper_location, game_state):
    """
    # do_jump function:
    #   Attempts to perform a jump into a gap on a given game board
    #   This function takes a gap location [row, position],
    #   a marble jumping candidate location, and a game state.
    #   Returns an updated game after the jump if possible.
    #   If not, returns a None value
    """

    gap_row, gap_positon = gap_location
    jumper_row, jumper_position = jumper_location
    jumper_state = game_state[jumper_row][jumper_position]

    # if jumper is a gap, cant jump
    if jumper_state == 0:
        return None
    # find state of positon in between jumper and gap
    jumped_row = int((gap_row + jumper_row) / 2)
    jumped_position = int((gap_positon + jumper_position) / 2)
    jumped_state = game_state[jumped_row][jumped_position]
    # if there is a marble, then allow jump
    if jumped_state == 1:
        updated_board = copy.deepcopy(game_state)
        updated_board[gap_row][gap_positon] = 1
        updated_board[jumped_row][jumped_position] = 0
        updated_board[jumper_row][jumper_position] = 0
        return updated_board
    return None


def check_for_win(game_state):
    """
    # check_for_win function:
    #   returns a boolean of whether or not a game state is winning
    """

    board_sum = 0
    for row in game_state:
        for position in row:
            board_sum += int(position)
    return board_sum == 1


def breadth_first_search(game_state, print_count=False, track_memory=False, verbose=False):
    """
    # breadth_first_search function:
    #   Finds a solution to given game_board.
    #   Takes and input of a 2D binary array  with a triangular structure.
    #   Can specifiy options of printing state count, memory use and verbosity.
    #
    #   Details:
    #       This function operates on a FIFO queue to operate as a
    #       breadth first search algorithm. It will check older states
    #       before newer children states. This will find the simpelest
    #       solution to the game.
    """

    game_states = [game_state]
    total_state_count = 0
    largest_state_tree = sys.getsizeof(game_states)
    if not verbose:
        while True:
            if len(game_states) == 0:  # check if there are anymore game states
                print(
                    "-- No more game states to check, no solution to starting board! --")
                stats_print(print_count, track_memory,
                            total_state_count, largest_state_tree)
                return None
            largest_state_tree = handle_tracking_memory(
                track_memory, game_states, largest_state_tree)
            current_state = game_states.pop(0)  # first out of queue
            total_state_count += 1
            if check_for_win(current_state):
                stats_print(print_count, track_memory,
                            total_state_count, largest_state_tree)
                return current_state
            for state in find_updated_boards(current_state):
                game_states.append(state)  # add newer states to end of queue
    else:  # same as above code, but more verbose
        marble = 'O'
        gap = '_'
        while True:
            if len(game_states) == 0:
                print(
                    "-- No more game states to check, no solution to starting board! --")
                stats_print(print_count, track_memory,
                            total_state_count, largest_state_tree)
                return None
            largest_state_tree = handle_tracking_memory(
                track_memory, game_states, largest_state_tree)
            current_state = game_states.pop(0)
            total_state_count += 1
            print('-- Finding moves on current state: --')
            visualize(current_state, marble, gap)
            if check_for_win(current_state):
                print('-- Found a Winner! -- ')
                stats_print(print_count, track_memory,
                            total_state_count, largest_state_tree)
                return current_state
            print('- Not a winnner, checking more states... -')
            new_states = find_updated_boards(current_state)
            new_states_length = len(new_states)
            if new_states_length == 0:
                print("- No more moves for current state, backing up... -")
            else:
                print(f'- Found {new_states_length} states: -')
                for state_index, state in enumerate(new_states_length):
                    print(f"  Move {state_index + 1}:")
                    visualize(state, marble, gap)
                    game_states.append(state)


def handle_tracking_memory(track_memory, game_states, largest_state_tree):
    """
    # track_memory function
    #   handles memory tracking
    """
    if track_memory:  # if tracking memory
        largest_state_tree = sys.getsizeof(game_states) if sys.getsizeof(
            game_states) > largest_state_tree else largest_state_tree
    return largest_state_tree


def stats_print(print_count, track_memory, total_state_count, largest_state_tree):
    """
    # stats_print function:
    #   handlings printing of stats for search function
    """
    if print_count:
        print(
            f'-- Number of states examined: {total_state_count:,} --')
    if track_memory:
        print(
            f'-- Largest state tree at any point: {largest_state_tree/1000:.2f} kB --')


if __name__ == '__main__':
    # Strings to represent positions
    MARBLE = 'O'
    GAP = '_'

    print("--- Starting board: ---")
    game_board = [
        [1],
        [1, 1],
        [1, 0, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ]
    visualize(game_board, MARBLE, GAP)

    print("--- Solved board: ---")
    visualize(breadth_first_search(
        game_board, print_count=True, track_memory=True, verbose=False), MARBLE, GAP)
