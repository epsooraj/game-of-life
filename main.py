import sys
import pygame
from pygame.locals import KEYDOWN, K_q
import numpy as np

from gol import generate_next_state

# CONSTANTS:
SCREENSIZE = WIDTH, HEIGHT = 1000, 1000
BLACK = (0, 0, 0)
GREY = (160, 160, 160)

# OUR GRID MAP:
# cellMAP = np.random.randint(2, size=(50, 50))
cellMAP = np.eye(50, dtype=int)

_VARS = {'surf': False, 'gridWH': 1000,
         'gridOrigin': (0, 0), 'gridCells': cellMAP.shape[0], 'lineWidth': 2}

FPS = 1


def main():

    global cellMAP
    global _VARS

    pygame.init()
    pygame.display.set_caption('Math')
    clock = pygame.time.Clock()
    _VARS['surf'] = pygame.display.set_mode(SCREENSIZE)
    while True:
        cellMAP = generate_next_state(cellMAP)
        checkEvents()
        _VARS['surf'].fill(GREY)
        _VARS['gridCells'] = cellMAP.shape[0]
        drawSquareGrid(
            _VARS['gridOrigin'], _VARS['gridWH'], _VARS['gridCells'])
        placeCells()
        pygame.display.update()
        clock.tick(FPS)


# NEW METHOD FOR ADDING CELLS :
def placeCells():
    # GET CELL DIMENSIONS...
    cellBorder = 1
    celldimX = celldimY = (_VARS['gridWH']/_VARS['gridCells']) - (cellBorder*2)
    # DOUBLE LOOP
    for row in range(cellMAP.shape[0]):
        for column in range(cellMAP.shape[1]):
            # Is the grid cell tiled ?
            if(cellMAP[column][row] == 1):
                drawSquareCell(
                    _VARS['gridOrigin'][0] + (celldimY*row)
                    + cellBorder + (2*row*cellBorder) + _VARS['lineWidth']/2,
                    _VARS['gridOrigin'][1] + (celldimX*column)
                    + cellBorder + (2*column*cellBorder) +
                    _VARS['lineWidth']/2,
                    celldimX, celldimY)

# Draw filled rectangle at coordinates


def drawSquareCell(x, y, dimX, dimY):
    pygame.draw.rect(
        _VARS['surf'], BLACK,
        (x, y, dimX, dimY)
    )


def drawSquareGrid(origin, gridWH, cells):

    CONTAINER_WIDTH_HEIGHT = gridWH
    cont_x, cont_y = origin

    # DRAW Grid Border:
    # TOP lEFT TO RIGHT
    pygame.draw.line(
        _VARS['surf'], BLACK,
        (cont_x, cont_y),
        (CONTAINER_WIDTH_HEIGHT + cont_x, cont_y), _VARS['lineWidth'])
    # # BOTTOM lEFT TO RIGHT
    pygame.draw.line(
        _VARS['surf'], BLACK,
        (cont_x, CONTAINER_WIDTH_HEIGHT + cont_y),
        (CONTAINER_WIDTH_HEIGHT + cont_x,
            CONTAINER_WIDTH_HEIGHT + cont_y), _VARS['lineWidth'])
    # # LEFT TOP TO BOTTOM
    pygame.draw.line(
        _VARS['surf'], BLACK,
        (cont_x, cont_y),
        (cont_x, cont_y + CONTAINER_WIDTH_HEIGHT), _VARS['lineWidth'])
    # # RIGHT TOP TO BOTTOM
    pygame.draw.line(
        _VARS['surf'], BLACK,
        (CONTAINER_WIDTH_HEIGHT + cont_x, cont_y),
        (CONTAINER_WIDTH_HEIGHT + cont_x,
            CONTAINER_WIDTH_HEIGHT + cont_y), _VARS['lineWidth'])

    # Get cell size, just one since its a square grid.
    cellSize = CONTAINER_WIDTH_HEIGHT/cells

    # VERTICAL DIVISIONS: (0,1,2) for grid(3) for example
    for x in range(cells):
        pygame.draw.line(
            _VARS['surf'], BLACK,
            (cont_x + (cellSize * x), cont_y),
            (cont_x + (cellSize * x), CONTAINER_WIDTH_HEIGHT + cont_y), 2)
    # # HORIZONTAl DIVISIONS
        pygame.draw.line(
            _VARS['surf'], BLACK,
            (cont_x, cont_y + (cellSize*x)),
            (cont_x + CONTAINER_WIDTH_HEIGHT, cont_y + (cellSize*x)), 2)


def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    main()