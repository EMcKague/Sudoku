import itertools


def finish(array_board):
    """Checks if given board is a valid solution
    """
    print_board(array_board)

    bad_rows = [row for row in array_board if not valid_row_col_or_square(row)]
    array_board = list(zip(*array_board))
    bad_cols = [col for col in array_board if not valid_row_col_or_square(col)]
    squares = []
    for i in range(0, 9, 3):
        for ii in range(0, 9, 3):
            square = list(itertools.chain(row[ii:ii+3]
                          for row in array_board[i:i+3]))
            squares.append(square)
    squares = convert(squares)
    bad_squares = [square for square in squares
                   if not valid_row_col_or_square(square)]

    return not(bad_cols or bad_rows or bad_squares)


def valid_row_col_or_square(some_list):
    return (len(some_list) == 9 and sum(some_list) == 45)


def print_board(array_board):
    rowNum = 0
    for row in array_board:
        temp = []
        for el in row:
            temp.append(str(el))
        print(
              # rowNum + 1,
              " ", '|'.join(temp[0:3]),
              " ", '|'.join(temp[3:6]),
              " ", '|'.join(temp[6:]))
        rowNum += 1
        if rowNum % 3 == 0:
            print()
    print('\n')


def solve(array_board):
    empty_square = find_empty_square(array_board)
    if not empty_square:
        return True

    row, col = empty_square
    for i in range(1, 10):
        if valid_sol(array_board, i, (row, col)):
            array_board[row][col] = i

            if solve(array_board):
                return True

            array_board[row][col] = 0

    return False


def valid_sol(array_board, num, pos):
    row, col = pos
    for i in range(9):
        if array_board[row][i] == num and col != i:
            return False

    for i in range(9):
        if array_board[i][col] == num and row != i:
            return False

    y = row // 3
    x = col // 3

    for i in range(y * 3, y * 3 + 3):
        for ii in range(x * 3, x * 3 + 3):
            if array_board[i][ii] == num and (i, ii) != pos:
                return False

    return True


def find_empty_square(array_board):
    for i in range(len(array_board)):
        for ii in range(len(array_board[i])):
            if array_board[i][ii] == 0:
                return (i, ii)


def convert(squares):
    temp = []
    for el in squares:
        temp2 = []
        for tup in el:
            for num in tup:
                temp2.append(num)
        temp.append(temp2)
    return temp
