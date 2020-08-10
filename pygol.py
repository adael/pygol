import numpy
import pygame

SW = 1000
SH = 800
SIZE = 10
COLS = int(SW / SIZE)
ROWS = int(SH / SIZE)
white = (255, 255, 255)
gray = (128, 128, 128)
black = (0, 0, 0)
paused = False
ranges = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (+1, 0),
    (-1, 1), (0, 1), (1, 1)
]

def start_game():
    global running, screen, gameState, newGameState, clock, font

    running = True
    pygame.init()
    pygame.display.set_caption("Game Of Life")
    screen = pygame.display.set_mode((SW, SH))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 18, bold=True)

    gameState = numpy.zeros((COLS, ROWS))
    newGameState = numpy.copy(gameState)


def stop_game():
    global running
    running = False
    pygame.quit()


def handle_events():
    mouse_events()

    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        handle_event(event)

def mouse_events():
    px, py = pygame.mouse.get_pos()
    m1, _, m2 = pygame.mouse.get_pressed()
    cx = int(px/SIZE)
    cy = int(py/SIZE)

    if m1:
        newGameState[cx][cy] = 1

    if m2:
        newGameState[cx][cy] = 0

def handle_event(event):
    global running, paused
    if event.type == pygame.QUIT:
        stop_game()
        return

    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            paused = not paused


def draw_grid():
    xs = 0
    xf = COLS * SIZE
    ys = 0
    yf = ROWS * SIZE
    for y in range(0, ROWS):
        pygame.draw.line(screen, gray, (xs, y*SIZE), (xf, y*SIZE))
    for x in range(0, COLS):
        pygame.draw.line(screen, gray, (x*SIZE, ys), (x*SIZE, yf))

    pygame.draw.rect(screen, gray, pygame.Rect(0, 0, xf, yf), 1)


def make_cell(x, y):
    return [
        (x * SIZE, y * SIZE),
        ((x+1) * SIZE, y * SIZE),
        ((x+1) * SIZE, (y+1) * SIZE),
        (x * SIZE, (y+1) * SIZE)
    ]


def process_cells():
    global gameState
    gameState = numpy.copy(newGameState)
    if not paused:
        for y in range(0, ROWS):
            for x in range(0, COLS):
                process_cell(x, y)


def process_cell(x, y):
    n = count_neighbours(x, y)
    if n == 3:
        newGameState[x][y] = 1
    elif n < 2 or n > 3:
        newGameState[x][y] = 0


def draw_cells():
    for y in range(0, ROWS):
        for x in range(0, COLS):
            draw_cell(x, y)


def draw_cell(x, y):
    if gameState[x][y]:
        cell = make_cell(x, y)
        pygame.draw.polygon(screen, white, cell, 0)


def count_neighbours(x, y):
    n = 0

    for (mx, my) in ranges:
        px = mx+x
        py = my+y


        if px >= 0 and py >= 0 and px < COLS and py < ROWS:
            n += gameState[px][py]

    return n


def draw_fps():
    fps = str(int(clock.get_fps())) + " FPS, Total: " + str(ROWS*COLS)
    fps_text = font.render(fps, 1, pygame.Color("orange"))
    screen.blit(fps_text, (10, 0))


def game_loop():
    start_game()
    while running:
        clock.tick()
        screen.fill(black)
        draw_grid()
        draw_fps()
        process_cells()
        draw_cells()
        pygame.display.flip()
        handle_events()


game_loop()
