import numpy as np

i, j = 70, 70


def generate_glider():

    gi = 5
    gj = 5

    lives = np.zeros((i, j), dtype=int)

    lives[gi + 4, gj + 0] = 1
    lives[gi + 4, gj + 1] = 1
    lives[gi + 5, gj + 0] = 1
    lives[gi + 5, gj + 1] = 1

    lives[gi + 2, gj + 12] = 1
    lives[gi + 2, gj + 13] = 1

    lives[gi + 3, gj + 11] = 1

    lives[gi + 4, gj + 10] = 1
    lives[gi + 5, gj + 10] = 1
    lives[gi + 6, gj + 10] = 1

    lives[gi + 7, gj + 11] = 1
    lives[gi + 8, gj + 12] = 1
    lives[gi + 8, gj + 13] = 1

    lives[gi + 5, gj + 14] = 1

    lives[gi + 3, gj + 15] = 1
    lives[gi + 4, gj + 16] = 1
    lives[gi + 5, gj + 16] = 1
    lives[gi + 5, gj + 17] = 1
    lives[gi + 6, gj + 16] = 1
    lives[gi + 7, gj + 15] = 1

    lives[gi + 1, gj + 22] = 1
    lives[gi + 2, gj + 20] = 1
    lives[gi + 3, gj + 20] = 1
    lives[gi + 4, gj + 20] = 1
    lives[gi + 2, gj + 21] = 1
    lives[gi + 3, gj + 21] = 1
    lives[gi + 4, gj + 21] = 1
    lives[gi + 5, gj + 22] = 1

    lives[gi + 0, gj + 24] = 1
    lives[gi + 1, gj + 24] = 1

    lives[gi + 5, gj + 24] = 1
    lives[gi + 6, gj + 24] = 1

    lives[gi + 2, gj + 34] = 1
    lives[gi + 3, gj + 34] = 1
    lives[gi + 2, gj + 35] = 1
    lives[gi + 3, gj + 35] = 1

    return lives


def initialize_life_state():
    # Generate a array pattern
    # 1 = alive
    # 0 = dead

    # lives = np.zeros((i, j), dtype=int)
    # lives[i//2, j//2] = 1
    # lives[i//2+1, j//2+1] = 1
    # lives[i//2+2, j//2-1] = 1
    # lives[i//2+2, j//2] = 1
    # lives[i//2+2, j//2+1] = 1

    lives = generate_glider()

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
