board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board():
    """Prints the board to the console"""
    global board

    for r in  range(9):
        if r % 3 == 0 and r != 0:
            print("- - - - - - - - - - - ")

        for e in range(9):
            # Place a line after the 3rd number in each row
            if e % 3 == 0 and e != 0:
                print("| ", end = "")
            # Check if its the last number in row, print the number and start new line
            if e == 8:
                print(board[r][e])
            # Print number
            else:
                print(str(board[r][e]) + " ", end = "")


def validate(y, x, num):
    """Validates a number in a row"""
    global board

    # Check row
    for i in range(9):
        if board[y][i] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][x] == num:
            return False

    # Check square
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[y0 + i][x0 + j] == num:
                return False

    return True

def solve():
    """Solves puzzle using backtracking"""
    global board

    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for n in range(1, 10):
                    if validate(y, x, n):
                        board[y][x] = n
                        solve()
                        board[y][x] = 0
                return
    print("Solution")
    print_board()
    input("Press enter for more solutions")


print("Original")
print_board()
solve()