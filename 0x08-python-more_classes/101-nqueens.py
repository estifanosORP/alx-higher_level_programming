#!/usr/bin/python3
"""
Place N on-attacking queens on a NxN chessboard.
"""


def checker(board, row_idx, cols, pos):
    """
    checks if a queen could be placed at
    a specific position in a row
    """
    # Could be placed anywhere on the first row
    if row_idx == 0:
        return True
    # Coordinates of previous placements
    crds = [(x, cols[x]) for x in range(len(cols))]

    # Can't put on cols that already have queens
    if (pos in cols):
        return False
    # Check if the pos lies at a diagonal to other queens
    not_equal = [abs(ele[0]-row_idx) != abs(ele[1] - pos)  for ele in crds]
    if not all(not_equal):
        return False

    return True


def backtrack(board, row_idx, cols, N):
    """
    Go to the previous row and relocate the Queen
    """

    row_idx -= 1
    lst_pos = cols.pop()
    board[row_idx][lst_pos] = 0
    if lst_pos == N-1:
        board, row_idx, cols, lst_pos = backtrack(board, row_idx, cols, N)
    return board, row_idx, cols, lst_pos


def NQueen(N):
    """
    prints all the possible cooridnates of the N queens
    in the NxN chess board
    """

    # Dict to save all the solutions in list of lists
    all_solutions = {}
    # Initialize the first column to place the queen at each row
    start = 0
    # Loop until all solutions are found
    while start < N-1:

        board = [[0 for x in range(N)] for y in range(N)]
        row_idx = 0
        cols = []
        back_tracked = False
        lst_pos = 0

        while row_idx < N:
            row = board[row_idx]

            for pos in range(lst_pos+1 if back_tracked else start, N):
                start = 0
                back_tracked = False

                if checker(board, row_idx, cols, pos):
                    row[pos] = 1
                    cols.append(pos)
                    row_idx += 1
                    break

                if (pos == N-1):
                    board, row_idx, cols, lst_pos = backtrack(board,
                                                              row_idx,
                                                              cols,
                                                              N)
                    back_tracked = True

        start = board[0].index(1)+1
        all_solutions["sln" + str(start)] = board

    # Extract the positions of the the queens 
    for soln in all_solutions.values():
        index_solution = []
        for x in range(len(soln)):
            for y in range(len(soln[x])):
                if soln[x][y] == 1:
                    index_solution.append([x, y])
        print(index_solution)


if __name__ == '__main__':
    """
    main program
    """
    import sys

    arg_all = sys.argv
    if len(arg_all) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    # print the location of the queens
    NQueen(N)
