# CS481 Assignment 2

This project solves, visualizes, and collects statistics on games of triangle marble solitaire in [Python](python.org).

## Information

### Included files

* marble_game.py
  * main file which runs a search
* marble_game_timing.py
  * file which calls marble_game with different initals states
  * tracks and averages time to complete searches
* final.txt
  * the output of 'python marble_game.py' (not verbose)
* screen_shot.png
  * a screen shot of output of 'python marble_game.py' (not verbose)
* final_verbose.txt
  * the output of 'python marble_game.py' (verbose)
  * note: this file is large
* final_timings.txt
  * the output of 'python marble_game_timing.py'
* README.md
  * this file

### Statistics

Using a BFS algorithm, marble_game.py will examine up to appx. 2.5M states depending on the initial game board. The largest state tree at any one point will be less than 7.2 MB. These large numbers are due to almost no optimization of storage or processing included. To reduce size, a simpiler storage of the states could be made, storing only gap positons. To reduce the number of states examined, duplicate states could be removed.

## Usage

### To run the search algorithm

    python ./marble_game.py    # or see import usage in marble_game.py

### To test the algorithm

    python ./marble_game_timing.py  # to run a search on all possible boards with one gap (SLOW!)(Must have numpy installed)

## Help

email me @ migl8239@kXXX.edu for information or access
