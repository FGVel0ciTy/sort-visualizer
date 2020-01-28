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

default_display_width = 800
default_display_height = 800
default_grid_width = 100
default_grid_height = 100
tile_width = default_display_width // default_grid_width
tile_height = default_display_height // default_grid_height

os.environ['SDL_VIDEO_CENTERED'] = "0"
pygame.init()
screen = pygame.display.set_mode((default_display_width, default_display_height))
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
    def __init__(self, grid_width=100, grid_height=100, display_width=800, display_height=800):
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
