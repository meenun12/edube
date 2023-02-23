def validate_sudoku(sudoku):

    """
    This function validates a Sudoku solution.
    It checks if each row, column, and 3x3 subgrid contains only the digits 1-9,
    without repetition.
    The input should be a 9x9 grid, represented as a list of lists, where each
    inner list represents a row of the Sudoku grid.
    The function returns True if the solution is valid, and False otherwise.
    """

    # Check each row
    for row in sudoku:
        if len(set(row)) != 9 or any(x < 1 or x > 9 for x in row):
            return False

    # Check each column
    for i in range(9):
        column = [sudoku[j][i] for j in range(9)]
        if len(set(column)) != 9 or any(x < 1 or x > 9 for x in column):
            return False

    # Check each 3x3 subgrid
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [
                sudoku[x][y] for x in range(i, i + 3) for y in range(j, j + 3)
            ]
            if len(set(subgrid)) != 9 or any(x < 1 or x > 9 for x in subgrid):
                return False

    # If all checks pass, the Sudoku solution is valid
    return True

solution = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]

if validate_sudoku(solution):
    print("This is a valid Sudoku solution!")
else:
    print("This is not a valid Sudoku solution.")