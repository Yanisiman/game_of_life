import sys
import pygame
from random import randint

size = width, height = 800, 600
DEAD_COLOR = 0, 0, 0
ALIVE_COLOR = 255, 255, 255
CELL_SIZE = 10


class LifeGame:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        self.clear_screen()
        pygame.display.flip()
        self.width = width
        self.height = height
        self.cols = width // CELL_SIZE
        self.rows = height // CELL_SIZE
        self.grid = [[(1 if randint(0,100) < 10 else 0) for _ in range(self.cols)]for _ in range(self.rows)]

    def clear_screen(self):
        self.screen.fill(DEAD_COLOR)

    def countNeighbors(self, x, y):
        sum = 0
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                col = (x + i + self.cols) % self.cols
                row = (y + j + self.rows) % self.rows
                sum += self.grid[row][col]
        sum -= self.grid[y][x]
        return sum

    def update_generation(self):
        next = self.grid.copy()
        for r in range(self.rows):
            for c in range(self.cols):
                state = self.grid[r][c]
                neighbors = self.countNeighbors(c, r)
                if state == 0 and neighbors == 3:
                    next[r][c] = 1
                elif state == 1 and (neighbors < 2 or neighbors > 3):
                    next[r][c] = 0
                else:
                    next[r][c] = self.grid[r][c]

        self.grid = next

    def draw_grid(self):
        for r in range(self.rows):
            for c in range(self.cols):
                color = ALIVE_COLOR if self.grid[r][c] else DEAD_COLOR
                pygame.draw.circle(self.screen,
                color,
                (int(c * CELL_SIZE + (CELL_SIZE//2)),
                int(r * CELL_SIZE + (CELL_SIZE//2))),
                CELL_SIZE//2, 0)
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def run(self):
        while True:
            self.handle_events()
            self.update_generation()
            self.draw_grid()


gol = LifeGame(width, height)
gol.run()