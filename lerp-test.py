import pygame
from random import Random
from math import pi, sin, cos
from util import lerp, smoothstep
CIRCLE = 2 * pi

rnd = Random(78978696463456)

size = 16
cell_size = 64

corners = []
for x in range(size + 1):
    corners.append(round(rnd.random() * 1000 % CIRCLE, 3))
cells = []
for c in range(size):
    cell = []
    for x in range(cell_size):
        r = []
        for i in range(2):
            sin_t = sin(corners[c+i])
            r.append((i * cell_size - x) * sin_t)
        lrp = lerp(r[0], r[1], x/cell_size)
        lrp_smooth = lerp(r[0], r[1], smoothstep(x/cell_size))
        cell.append((lrp, lrp_smooth, r))

    cells.append(cell)


pygame.init()
screen = pygame.display.set_mode((800, 800))
screen.fill((255, 255, 255))

for c in cells:
    print(c)

for c in range(size):
    for s in range(cell_size):
        p = cells[c][s]
        pygame.draw.circle(screen, (0, 255, 0), (c * cell_size + s, 400 + p[0]), 1)
        pygame.draw.circle(screen, (0, 255, 255), (c * cell_size + s, 440 + p[1]), 1)
        pygame.draw.circle(screen, (255, 0, 0), (c * cell_size + s, 540 + p[2][0] ), 1)
        pygame.draw.circle(screen, (0, 0, 255), (c * cell_size + s, 300 + p[2][1]), 1)
        pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
        pygame.display.flip()
