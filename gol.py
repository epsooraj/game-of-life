import numpy as np

i, j = 70, 70


def generate_glider(i_offset, j_offset):

    lives = np.zeros((i, j), dtype=int)

    lives[i_offset + 4, j_offset + 0] = 1
    lives[i_offset + 4, j_offset + 1] = 1
    lives[i_offset + 5, j_offset + 0] = 1
    lives[i_offset + 5, j_offset + 1] = 1

    lives[i_offset + 2, j_offset + 12] = 1
    lives[i_offset + 2, j_offset + 13] = 1

    lives[i_offset + 3, j_offset + 11] = 1

    lives[i_offset + 4, j_offset + 10] = 1
    lives[i_offset + 5, j_offset + 10] = 1
    lives[i_offset + 6, j_offset + 10] = 1

    lives[i_offset + 7, j_offset + 11] = 1
    lives[i_offset + 8, j_offset + 12] = 1
    lives[i_offset + 8, j_offset + 13] = 1

    lives[i_offset + 5, j_offset + 14] = 1

    lives[i_offset + 3, j_offset + 15] = 1
    lives[i_offset + 4, j_offset + 16] = 1
    lives[i_offset + 5, j_offset + 16] = 1
    lives[i_offset + 5, j_offset + 17] = 1
    lives[i_offset + 6, j_offset + 16] = 1
    lives[i_offset + 7, j_offset + 15] = 1

    lives[i_offset + 1, j_offset + 22] = 1
    lives[i_offset + 2, j_offset + 20] = 1
    lives[i_offset + 3, j_offset + 20] = 1
    lives[i_offset + 4, j_offset + 20] = 1
    lives[i_offset + 2, j_offset + 21] = 1
    lives[i_offset + 3, j_offset + 21] = 1
    lives[i_offset + 4, j_offset + 21] = 1
    lives[i_offset + 5, j_offset + 22] = 1

    lives[i_offset + 0, j_offset + 24] = 1
    lives[i_offset + 1, j_offset + 24] = 1

    lives[i_offset + 5, j_offset + 24] = 1
    lives[i_offset + 6, j_offset + 24] = 1

    lives[i_offset + 2, j_offset + 34] = 1
    lives[i_offset + 3, j_offset + 34] = 1
    lives[i_offset + 2, j_offset + 35] = 1
    lives[i_offset + 3, j_offset + 35] = 1

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

    lives = generate_glider(5, 5)

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
