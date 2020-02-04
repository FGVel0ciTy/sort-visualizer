import numpy
import pygame
import math
import random
import os
import sys
import time
import colorsys
import copy

red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
white = [255, 255, 255]
black = [0, 0, 0]

display_width = 600
display_height = 300
grid_width = 30
grid_height = 15
tile_width = display_width // grid_width
tile_height = display_height // grid_height

default_sleep_time = .1
sleep_time = default_sleep_time

os.environ['SDL_VIDEO_CENTERED'] = "0"
pygame.init()
screen = pygame.display.set_mode((display_width, display_height))
screen.fill(white)


class Tile:
    def __init__(self, coord1, coord2=0, color=white):
        if isinstance(coord1, int):
            self.x = coord1
            self.y = coord2
        else:
            self.x, self.y = coord1
        self.coord = [self.x, self.y]
        self.color = self.update_color(color)
        r, g, b = self.color
        self.hue = colorsys.rgb_to_hsv(r, g, b)[0]

    def __repr__(self):
        return f"Tile at {self.x}, {self.y} with {self.color} color"

    def update_color(self, color):
        self.color = color
        pygame.draw.rect(screen, color, (self.x * tile_width, self.y * tile_height, tile_width, tile_height))
        pygame.display.update((self.x * tile_width, self.y * tile_height, tile_width, tile_height))
        r, g, b = self.color
        self.hue = colorsys.rgb_to_hsv(r, g, b)[0]
        return self.color


grid = numpy.empty((grid_width, grid_height), object)

colors = []
for i in range(3):
    for j in range(3):
        temp_color = [0, 0, 0]
        temp_color[i] = 255
        if j != i:
            for k in range(0, 256, 51):
                temp_color[j] = k
                if temp_color not in colors:
                    colors.append(temp_color[:])
print(len(colors), colors)


def initialize():
    for y in range(grid_height):
        temp = colors[:]
        for x in range(grid_width):
            grid[x, y] = Tile(x, y, temp.pop(random.randint(0, len(temp) - 1)))
            print(grid[x, y])


def insertion_sort():
    for y in range(grid_height):
        for x in range(grid_width):
            min_x = x
            for next_x in range(x + 1, grid_width):
                if grid[min_x, y].hue > grid[next_x, y].hue:
                    min_x = next_x
            swap(grid[x, y], grid[min_x, y])


def swap(tile1, tile2):
    temp = tile2.color[:]
    tile2.update_color(tile1.color)
    time.sleep(sleep_time)
    tile1.update_color(temp)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F5:
                initialize()
            if event.key == pygame.K_RETURN:
                insertion_sort()
