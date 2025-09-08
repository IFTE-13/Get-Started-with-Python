# The 4-Queens problem is a simplified version of the N-Queens puzzle. Place 4 queens on a 4×4 chessboard such that no two queens threaten each other. A queen can attack any piece in the same row, column, or diagonal.

# Task: Write a Python program that:
# 1. Uses backtracking to place the 4 queens.
# 2. Prints one valid solution showing the chessboard as a 4×4 grid with 1 representing a queen and 0 representing an empty square.
# 3. If no solution exists, print "Not possible".

def NAQD():
    board = [[0, 0, 0, 0] for _ in range(4)]  # Initialize 4x4 chessboard

    if not solve(board, 0):
        print("Not possible")
        return False

    # Print the solution
    for row in board:
        print(row)
    return True


def secure(board, row, col):
    # Check left side of the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, 4, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve(board, col):
    # If all queens are placed
    if col >= 4:
        return True

    for i in range(4):
        if secure(board, i, col):
            board[i][col] = 1

            if solve(board, col + 1):
                return True

            board[i][col] = 0  # Backtrack

    return False


# Run the program
NAQD()
