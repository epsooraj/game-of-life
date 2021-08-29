import numpy as np


def initialize_life_state():
    i, j = 50, 50

    # Generate a array pattern
    # 1 = alive
    # 0 = dead

    lives = np.zeros((i, j), dtype=int)
    lives[i//2, j//2] = 1
    lives[i//2+1, j//2+1] = 1
    lives[i//2+2, j//2-1] = 1
    lives[i//2+2, j//2] = 1
    lives[i//2+2, j//2+1] = 1

    # lives = np.random.randint(2, size=(i, j))

    return lives


def generate_next_state(prevCells):
    cellMAP = np.zeros(prevCells.shape, dtype=int)

    for i in range(prevCells.shape[0]):
        for j in range(prevCells.shape[1]):
            cellMAP[i, j] = prevCells[i, j]
            if prevCells[i, j] == 1:
                # Death of cell
                # Check if cell is alone, less than 3 neighbors
                if np.sum(prevCells[i-1:i+2, j-1:j+2]) - 1 <= 1:
                    cellMAP[i, j] = 0

                # Death of cell
                # Check if cell is overcrowded, greater than 3 neighbors
                if np.sum(prevCells[i-1:i+2, j-1:j+2]) - 1 >= 4:
                    cellMAP[i, j] = 0

            # Birth of cell
            # Check if cell has 3 neighbors
            if prevCells[i, j] == 0:
                if np.sum(prevCells[i-1:i+2, j-1:j+2]) == 3:
                    cellMAP[i, j] = 1

    return cellMAP
