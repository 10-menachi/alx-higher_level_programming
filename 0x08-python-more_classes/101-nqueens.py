#!/usr/bin/python3

import sys


def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, N):
    if col == N:
        print_solution(board, N)
        return

    for row in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens_util(board, col + 1, N)
            board[row][col] = 0


def solve_nqueens(N):
    board = [[0] * N for _ in range(N)]
    solve_nqueens_util(board, 0, N)


def print_solution(board, N):
    solution = []
    for row in range(N):
        queen_pos = [str(row), str(board[row].index(1))]
        solution.append(",".join(queen_pos))
    print("[" + ", ".join(solution) + "]")


if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) != 1:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(args[0])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
