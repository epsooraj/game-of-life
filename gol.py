import numpy as np


def generate_next_state(prevCells):
    # cellMAP = np.random.randint(2, size=prevCells.shape)
    cellMAP = prevCells

    for i in range(prevCells.shape[0]):
        for j in range(prevCells.shape[1]):
            if cellMAP[i, j] == 1:
                cellMAP[i, j] = 0
            else:
                cellMAP[i, j] = 1

    return cellMAP
