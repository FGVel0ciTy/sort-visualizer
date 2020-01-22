import numpy
import pygame
import math
import random
import os
import sys
import time

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

display_width = 800
display_height = 800
grid_height = 100
grid_width = 100
tile_width = display_width // grid_width
tile_height = display_height // grid_height

os.environ['SDL_VIDEO_CENTERED'] = "0"
pygame.init()
screen = pygame.display.set_mode((display_width, display_height))
screen.fill(white)


class Tile:
    def __init__(self, coord1, coord2=0):
        if isinstance(coord1, int):
            self.x = coord1
            self.y = coord2
        else:
            self.x, self.y = coord1

    def set_color(self):
        pass


class Grid:
    def __init__(self, grid_width=100, grid_height=100):
        self.grid = grid = numpy.empty((grid_width, grid_height), object)
        for x in range(grid_width):
            for y in range(grid_height):
                grid[x, y] = Tile(x, y)
        self.grid_width = grid_width
        self.grid_height = grid_height


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
