# Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that
# each column, each row,and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the
# numbers from 1 to 9 one time.

# Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle
# according to the layout rules described above. Note that the puzzle represented by grid does not have
# to be solvable.


def sudoku2(grid):
    def check_validity(rows):
        for row in rows:
            if sum(row) != sum(set(row)):
                return False
        return True

    int_rows = [[int(x) for x in filter(lambda x: x != '.', row)] for row in grid]

    int_columns_to_rows = [[int(x) for x in filter(lambda x: x != '.', row)] for row in list(zip(*grid))]

    if not check_validity(int_rows) or not check_validity(int_columns_to_rows):
        return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = [grid[k][z] for k in range(i, i+3) for z in range(j, j+3)]

            square_int = [int(x) for x in square if x != '.']

            if sum(square_int) != sum(set(square_int)):
                return False
    return True
