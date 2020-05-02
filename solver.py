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

def print_board(brd):
    """Prints the board to the console"""
    for r in  range(len(brd)):
        if r % 3 == 0 and r != 0:
            print("- - - - - - - - - - - ")

        for c in range(len(brd[0])):
            # Place a line after the 3rd number in each row
            if c % 3 == 0 and c != 0:
                print("| ", end = "")
            # Check if its the last number in row, print the number and start new line
            if c == 8:
                print(brd[r][c])
            # Print number
            else:
                print(str(brd[r][c]) + " ", end = "")


def find_empty(brd):
    """Finds empty spaces in the sudoku puzzle and returns position"""
    for r in range(len(brd)):
        for c in range(len(brd[0])):
            if brd[r][c] == 0:
                return (r, c) # (Row, Column)

def validate(brd, num, pos):
    """Validates a number in a row"""
    # Check row
    for i in range(len(brd[0])):
        if brd[pos[0][i]] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(brd)):
        if brd[i][pos[0]] == num and pos[0] != i:
            return False

    # Check area
    




print_board(board)