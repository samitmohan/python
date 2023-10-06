# https://leetcode.com/problems/valid-sudoku/

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

'''
Documentation
  -> Keep a hashmap (set) and put all values of box in it, then check if it repeats for every row/column -> if it does -> not valid
  -> Check for every row (9) for every col (9) and also for every square,
  Defining Square
    instead of 0 1 2 .. 9 -> label them as 0 1 2 (col and rows), and to calc just // -> 4 row 4 col -> 4 // 3, 4 // 3 -> [1, 1] -> check at 1, 1

Time Complexity -> Hashsets for columns, rows, and each 3x3 square, O(1) time to check, iterating through the entire board (9*9) -> O(81)
'''

import collections


def isValidSudoku(board):
    # key, val = cols and set (empty for now)
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)  # key = (r / 3 and c / 3)
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                # empty -> ignore
                continue
            if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[
                (r // 3, c // 3)]):  # not valid
                return False
            # otherwise -> add in set
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])

    # went through all tests, it is a valid sudoku.
    return True


def main():
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(isValidSudoku(board))


main()
