# game_of_life.py
import random
import time
import os

def initialize_board(rows, cols):
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

def print_board(board):
    for row in board:
        print(' '.join(['#' if cell else ' ' for cell in row]))
    print('\n' + '-' * len(row) * 2 + '\n')

def update_board(board):
    new_board = [[0] * len(board[0]) for _ in range(len(board))]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            live_neighbors = sum([
                board[x % len(board)][y % len(board[0])]
                for x in range(i-1, i+2)
                for y in range(j-1, j+2)
            ]) - board[i][j]

            if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                new_board[i][j] = 0
            elif board[i][j] == 0 and live_neighbors == 3:
                new_board[i][j] = 1
            else:
                new_board[i][j] = board[i][j]

    return new_board

def main():
    rows = 40
    cols = 60
    generations = 50

    board = initialize_board(rows, cols)

    for _ in range(generations):
        os.system('clear' if os.name == 'posix' else 'cls')  # Clear the console
        print_board(board)
        time.sleep(0.2)  # Adjust the speed if needed
        board = update_board(board)

if __name__ == '__main__':
    main()
