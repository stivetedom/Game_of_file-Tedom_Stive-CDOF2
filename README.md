# Game_of_file-Tedom_Stive-CDOF2
The famous game by mathematician John Horton Conway. To make it console based, you can use spaces for dead cells and # for live cells.

### Game of Life Overview:
Objective:
The Game of Life is a cellular automaton devised by mathematician John Conway. It is a zero-player game, meaning that its evolution is determined by its initial state, with no further input from humans. The "players" in this game are the cells in a grid, and their state evolves based on simple rules.

### Rules:

Any live cell with fewer than two live neighbors dies (underpopulation).
Any live cell with two or three live neighbors survives.
Any live cell with more than three live neighbors dies (overpopulation).
Any dead cell with exactly three live neighbors becomes a live cell (reproduction).
# Code Explanation:
### initialize_board(rows, cols)
This function creates and returns an initial random game board with the specified number of rows and columns. Each cell is initialized as either alive (1) or dead (0).

### print_board(board)
Prints the current state of the board to the console, representing live cells with '#' and dead cells with a space. It adds a horizontal line to separate each generation for better visualization.

### update_board(board)
This function updates the board based on the Game of Life rules. It calculates the next state for each cell and creates a new board accordingly.

### main()
This is the main function that orchestrates the entire simulation. It sets up the initial board, prints each generation, and updates the board for a specified number of generations. The os.system line clears the console to create a smooth animation effect.

### __name__ == '__main__'
This conditional block ensures that the main() function is executed only if the script is run directly and not imported as a module.

How the Game Operates:
# Initialization:

The game starts with an initial random configuration of live and dead cells.
The board is printed, showing the initial state.
Animation Loop:

The main loop iterates through generations, printing each state to the console.
Cells evolve based on the rules of the Game of Life.
Visualization:

Live cells are represented by '#' and dead cells by spaces.
The console is cleared before printing each new generation, creating an animated effect.
Evolution:

The board evolves according to the rules, leading to patterns, stability, or eventual extinction.
Termination:

The simulation stops after a specified number of generations.
Project Objective:
The objective of this project is to create a console-based implementation of the Game of Life using Python. It aims to provide a functional and well-documented open-source project that others can easily understand, contribute to, and run on their machines. The use of a clear setup file (setup.py) and a chosen license (MIT) promotes good project management and collaboration within the open-source community.


## How to Run the Project
### Follow these steps to run the Game of Life on your machine:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/game-of-life.git
```

2. Navigate to the Project Directory:
``bash
cd game-of-life
```
3. Installation
Install package with pip
```bash
    pip import random
    pip import time
    pip import os

```

4. Run the Game of Life:
``bash
python game_of_life.p
```
