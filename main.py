import sys

import pygame
from pygame.constants import MOUSEWHEEL, K_n
from pygame.locals import KEYDOWN, K_q

from gol import generate_next_state, initialize_life_state

# Initialize Life State with pattern
cellMAP = initialize_life_state()

# CONSTANTS:
SCREENSIZE = WIDTH, HEIGHT = 1000, 1000
ALIVE_COLOR = (255, 255, 255)
DEAD_COLOR = (0, 0, 0)

_VARS = {'surf': False, 'gridWH': 1000,
         'gridOrigin': (0, 0), 'gridCells': cellMAP.shape[0], 'lineWidth': 0}

FPS = 60


def main():

    global cellMAP
    global _VARS

    pygame.init()
    pygame.display.set_caption('Game of Life')
    clock = pygame.time.Clock()
    _VARS['surf'] = pygame.display.set_mode(SCREENSIZE)
    while True:
        frame_step = checkEvents()
        _VARS['surf'].fill(DEAD_COLOR)
        drawSquareGrid(
            _VARS['gridOrigin'], _VARS['gridWH'], _VARS['gridCells'])
        placeCells()
        pygame.display.update()

        # if frame_step:
        cellMAP = generate_next_state(cellMAP)

        clock.tick(FPS)


def placeCells():
    '''
    METHOD FOR ADDING CELLS
    '''
    cellBorder = 1
    # GET CELL DIMENSIONS
    celldimX = celldimY = (_VARS['gridWH']/_VARS['gridCells']) - (cellBorder*2)

    for row in range(cellMAP.shape[0]):
        for column in range(cellMAP.shape[1]):
            if(cellMAP[column][row] == 1):
                drawSquareCell(
                    _VARS['gridOrigin'][0] + (celldimY*row)
                    + cellBorder + (2*row*cellBorder) + _VARS['lineWidth']/2,
                    _VARS['gridOrigin'][1] + (celldimX*column)
                    + cellBorder + (2*column*cellBorder) +
                    _VARS['lineWidth']/2,
                    celldimX, celldimY)


def drawSquareCell(x, y, dimX, dimY):
    '''
    Draw filled rectangle at coordinates
    '''
    pygame.draw.rect(
        _VARS['surf'], ALIVE_COLOR,
        (x, y, dimX, dimY)
    )


def drawSquareGrid(origin, gridWH, cells):

    CONTAINER_WIDTH_HEIGHT = gridWH
    cont_x, cont_y = origin

    # DRAW Grid Border:
    # TOP lEFT TO RIGHT
    pygame.draw.line(
        _VARS['surf'], ALIVE_COLOR,
        (cont_x, cont_y),
        (CONTAINER_WIDTH_HEIGHT + cont_x, cont_y), _VARS['lineWidth'])
    # # BOTTOM lEFT TO RIGHT
    pygame.draw.line(
        _VARS['surf'], ALIVE_COLOR,
        (cont_x, CONTAINER_WIDTH_HEIGHT + cont_y),
        (CONTAINER_WIDTH_HEIGHT + cont_x,
            CONTAINER_WIDTH_HEIGHT + cont_y), _VARS['lineWidth'])
    # # LEFT TOP TO BOTTOM
    pygame.draw.line(
        _VARS['surf'], ALIVE_COLOR,
        (cont_x, cont_y),
        (cont_x, cont_y + CONTAINER_WIDTH_HEIGHT), _VARS['lineWidth'])
    # # RIGHT TOP TO BOTTOM
    pygame.draw.line(
        _VARS['surf'], ALIVE_COLOR,
        (CONTAINER_WIDTH_HEIGHT + cont_x, cont_y),
        (CONTAINER_WIDTH_HEIGHT + cont_x,
            CONTAINER_WIDTH_HEIGHT + cont_y), _VARS['lineWidth'])

    # Get cell size, just one since its a square grid.
    cellSize = CONTAINER_WIDTH_HEIGHT/cells

    # VERTICAL DIVISIONS: (0,1,2) for grid(3) for example
    for x in range(cells):
        pygame.draw.line(
            _VARS['surf'], ALIVE_COLOR,
            (cont_x + (cellSize * x), cont_y),
            (cont_x + (cellSize * x), CONTAINER_WIDTH_HEIGHT + cont_y), 0)
    # # HORIZONTAl DIVISIONS
        pygame.draw.line(
            _VARS['surf'], ALIVE_COLOR,
            (cont_x, cont_y + (cellSize*x)),
            (cont_x + CONTAINER_WIDTH_HEIGHT, cont_y + (cellSize*x)), 0)


def checkEvents():
    '''
    Keyboard, Mouse events
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_n:
            return True
        elif event.type == MOUSEWHEEL:
            print(event)
            print(event.x, event.y)
            print(event.flipped)
            print(event.which)


if __name__ == '__main__':
    main()
