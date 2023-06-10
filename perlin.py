from math import sin, cos, pi
from util import smoothstep, lerp
import pygame
from random import Random

CIRCLE = 2 * pi


def pixel(corner, y, x, pos):
    dy = y - pos[0]
    dx = x - pos[1]
    return dy * corner[0] + dx * corner[1]


def perlin(rnd, cell_range, cell_size):
    grid_size = cell_range + 1
    size = cell_size * cell_range
    corners = []
    for y in range(grid_size):
        row = []
        for x in range(grid_size):
            theta = round(rnd.random() * 1000 % CIRCLE, 3)
            row.append((sin(theta), cos(theta)))
        corners.append(row)
    cells = []

    for y in range(cell_range):
        cell_row = []
        for x in range(cell_range):
            cell = []
            for yp in range(cell_size):
                row = []
                ypn = (yp + 1) / cell_size
                for xp in range(cell_size):
                    xpn = (xp + 1) / cell_size

                    top_left = pixel(corners[y][x], ypn, xpn, (0, 0))
                    top_right = pixel(corners[y][x+1], ypn, xpn, (0, 1))
                    bot_left = pixel(corners[y+1][x], ypn, xpn, (1, 0))
                    bot_right = pixel(corners[y+1][x+1], ypn, xpn, (1, 1))

                    top = lerp(top_left, top_right, smoothstep(xpn))
                    bot = lerp(bot_left, bot_right, smoothstep(xpn))
                    full = lerp(top, bot, smoothstep(ypn))
                    row.append(full)
                cell.append(row)
            cell_row.append(cell)
        cells.append(cell_row)

    pixels = []
    for y in range(cell_range):
        for yp in range(cell_size):
            row = []
            for x in range(cell_range):
                    for xp in range(cell_size):
                        p = cells[y][x][yp][xp] / 2 + 0.5
                        row.append(p)
            pixels.append(row)
    return pixels


CELL_RANGE = 8
CELL_SIZE = 64
SEED = 486758364563456
if __name__ == "__main__":
    size = CELL_SIZE * CELL_RANGE
    m = perlin(Random(SEED), CELL_RANGE, CELL_SIZE)
    pygame.init()
    screen = pygame.display.set_mode((size, size))

    for y in range(size):
        for x in range(size):
            p = m[y][x]
            """
            r = 255 * p
            g = 128
            b = 255 - r / 4
            screen.set_at((x, y), (r, g, b))
            """
            if round(p*33) % 7 == 0:
                screen.set_at((x, y), (255, 255, 255))


        pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit(0)
            pygame.display.flip()

