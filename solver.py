import pprint


def solve(board):
    """
    Solve a board using the backtracking algorithm
    :params bo: board as a 2-dim list of ints
    :returns: solution
    """

    # see if there any empty
    find = get_empty(board)

    if find:
        row, col = find
    else:
        return True

    for i in range(1, 10):
        if valid(board, (row, col), i):
            board[row][col] = i

            if solve(board) is not None:
                return board

            board[row][col] = 0


def valid(board, pos, num):
    """
    Returns if the given move is valid
    :params board: 2dim list of ints
    :params pos: position as a row-column pair
    :params num: int to test
    """

    # check row
    for i in range(0, len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(0, len(board)):
        if board[i][pos[1]] == num and pos[1] != i:
            return False

    # check box
    boxx = pos[1] // 3
    boxy = pos[0] // 3

    for i in range(boxy * 3, boxy * 3 + 3):
        for j in range(boxx * 3, boxx * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def get_empty(board):
    """
    Gets the next empty spot, or returns None
    :params bo: boards as a 2dim list of ints
    :returns: pos None
    """

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                # position using a tuple, to ensure that the variable is immutable
                pos = (i, j)
                return pos

    return None


easy_sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

pprint.pprint(solve(easy_sudoku))
