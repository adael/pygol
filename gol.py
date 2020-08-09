import numpy
import pygame

SW = 1000
SH = 800
SIZE = 25
COLS = int(SW / SIZE)
ROWS = int(SH / SIZE)
white = (255, 255, 255)
gray = (128, 128, 128)
black = (0, 0, 0)

gameState = numpy.zeros((COLS, ROWS))


def makeCell(x, y):
    return [
        (x * SIZE, y * SIZE),
        ((x+1) * SIZE, y * SIZE),
        ((x+1) * SIZE, (y+1) * SIZE),
        (x * SIZE, (y+1) * SIZE)
    ]


def makeGrid(screen):
    for x in range(0, COLS):
        for y in range(0, ROWS):
            cell = makeCell(x,y)
            pygame.draw.polygon(screen, gray, cell, 1)

def contarVecinos(gameState, x, y):
    pass

def run():
    pygame.init()
    screen = pygame.display.set_mode((SW, SH))
    pygame.display.set_caption("Game Of Life")

    while True:
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill(black)
        vecinos = contarVecinos(gameState, x, y)
        makeGrid(screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    run()
