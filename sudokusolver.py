import numpy as np


sudoku = [[2, 0, 0, 0, 0, 0, 0, 6, 0],
          [0, 0, 0, 0, 7, 5, 0, 3, 0],
          [0, 4, 8, 0, 9, 0, 1, 0, 0],
          [0, 0, 0, 3, 0, 0, 0, 0, 0],
          [3, 0, 0, 0, 1, 0, 0, 0, 9],
          [0, 0, 0, 0, 0, 8, 0, 0, 0],
          [0, 0, 1, 0, 2, 0, 5, 7, 0],
          [0, 8, 0, 7, 3, 0, 0, 0, 0],
          [0, 9, 0, 0, 0, 0, 0, 0, 4]]


def check(x, y, n):
    # check column
    for i in range(9):
        if sudoku[x][i] == n:
            return False
    # check row
    for i in range(9):
        if sudoku[i][y] == n:
            return False
    # check square
    x_sq = (x // 3) * 3
    y_sq = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[x_sq+i][y_sq+j] == n:
                return False
    return True


def solve():
    # for each column
    for i in range(9):
        # for each row
        for j in range(9):
            if sudoku[i][j] == 0:
                for n in range(1, 10):
                    if check(i, j, n):
                        sudoku[i][j] = n
                        # recursive calling of solve()
                        solve()
                        # if check() false -> backtracking
                        sudoku[i][j] = 0
                return
    print(np.matrix(sudoku))


solve()
