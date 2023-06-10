from perlin import perlin
from random import Random
import pygame
from util import merge
from threading import Thread


class PerlinThread(Thread):
    def __init__(self, seed, cell_range, cell_size):
        super().__init__()
        self.rnd = Random(seed)
        self.cell_range = cell_range
        self.cell_size = cell_size
        self.out = []

    def run(self) -> None:
        self.out = perlin(self.rnd, self.cell_range, self.cell_size)


if __name__ == "__main__":

    seed = 34534525432

    t1 = PerlinThread(seed, 8, 128)
    t2 = PerlinThread(seed, 32, 32)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    mp = t1.out
    mp2 = t2.out
    mp3 = merge(mp, mp2, lambda a, b: 3 * a * a * a + b*b*b / 8)
    size = len(mp3)
    pygame.init()
    window = pygame.display.set_mode((size, size), pygame.RESIZABLE)
    screen = pygame.surface.Surface((size, size))
    screen.fill((0, 0, 0))

    for y in range(size):
        for x in range(size):
            p = mp3[y][x]
            if p < 0.3:
                color = (80 * p, 185 * p, 255 * p * 1.5)
            elif p < 0.4:
                color = (240, 220, 150)
            elif p < 0.9:
                color = (35, 95, 54)
            else:
                color = (100, 120, 100)
            screen.set_at((x, y), color)
        window.blit(pygame.transform.scale(screen, window.get_rect().size), (0, 0))
        pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit(0)

        window.blit(pygame.transform.scale(screen, window.get_size()), (0, 0))
        pygame.display.flip()
