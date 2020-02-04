import numpy
import pygame
import math
import random
import os
import sys
import time
import colorsys

red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
white = [255, 255, 255]
black = [0, 0, 0]


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
        try:
            if self.color != color:
                time.sleep(step_time)
        except AttributeError:
            pass
        self.color = color
        pygame.draw.rect(screen, color, (self.x * tile_width, self.y * tile_height, tile_width, tile_height))
        pygame.display.update((self.x * tile_width, self.y * tile_height, tile_width, tile_height))
        r, g, b = self.color
        self.hue = colorsys.rgb_to_hsv(r, g, b)[0]
        return self.color


def make_board():
    for y in range(grid_height):
        temp = colors[:]
        for x in range(grid_width):
            grid[x, y] = Tile(x, y, temp.pop(random.randint(0, len(temp) - 1)))


def selection_sort():
    for y in range(grid_height):
        for x in range(grid_width):
            min_x = x
            for next_x in range(x + 1, grid_width):
                if grid[min_x, y].hue > grid[next_x, y].hue:
                    min_x = next_x
            swap(grid[x, y], grid[min_x, y])


def insertion_sort():
    for y in range(grid_height):
        for x in range(1, grid_width):
            current_hue = grid[x, y].hue
            current_col = grid[x, y].color[:]
            x_before = x - 1
            while x_before >= 0 and current_hue < grid[x_before, y].hue:
                grid[x_before + 1, y].update_color(grid[x_before, y].color)
                x_before -= 1
            grid[x_before + 1, y].update_color(current_col)


def bubble_sort():
    for y in range(grid_height):
        for x in range(grid_width):
            swapped = False
            for current_x in range(0, grid_width - x - 1):
                if grid[current_x, y].hue > grid[current_x + 1, y].hue:
                    swap(grid[current_x, y], grid[current_x + 1, y])
                    swapped = True

            if not swapped:
                break


def merge_sort():
    for y in range(grid_height):
        merge_sort_helper(list(range(0, grid_width)), y)


def merge_sort_helper(indices, row):
    if len(indices) > 1:
        mid = len(indices) // 2
        left = indices[:mid]
        right = indices[mid:]

        merge_sort_helper(left, row)
        merge_sort_helper(right, row)
        left = [[grid[idx, row].color, grid[idx, row].hue] for idx in left]
        right = [[grid[idx, row].color, grid[idx, row].hue] for idx in right]

        cur_l = cur_r = cur_ovrll = 0

        while cur_l < len(left) and cur_r < len(right):
            if left[cur_l][1] < right[cur_r][1]:
                grid[indices[cur_ovrll], row].update_color(left[cur_l][0])
                cur_l += 1
            else:
                grid[indices[cur_ovrll], row].update_color(right[cur_r][0])
                cur_r += 1
            cur_ovrll += 1

        while cur_l < len(left):
            grid[indices[cur_ovrll], row].update_color(left[cur_l][0])
            cur_l += 1
            cur_ovrll += 1

        while cur_r < len(right):
            grid[indices[cur_ovrll], row].update_color(right[cur_r][0])
            cur_r += 1
            cur_ovrll += 1


def swap(tile1, tile2):
    temp = tile2.color[:]
    tile2.update_color(tile1.color)
    tile1.update_color(temp)


def change_sort(index):
    global current_sort_index
    if index == "next":
        if current_sort_index >= len(sorts) - 1:
            current_sort_index = 0
        else:
            current_sort_index += 1
    elif index == "back":
        if current_sort_index <= 0:
            current_sort_index = len(sorts) - 1
        else:
            current_sort_index += -1
    else:
        current_sort_index = index
    pygame.display.set_caption(f"{sort_names[current_sort_index]} Sort")


sort_names = [
    "Selection",
    "Insertion",
    "Bubble",
    "Merge"
]
sorts = [
    selection_sort,
    insertion_sort,
    bubble_sort,
    merge_sort
]

display_width = 600
display_height = 200
grid_width = 30
grid_height = 10
tile_width = display_width // grid_width
tile_height = display_height // grid_height

default_step_time = .01
step_show = True
step_time = default_step_time

os.environ['SDL_VIDEO_CENTERED'] = "0"
pygame.init()
screen = pygame.display.set_mode((display_width, display_height))
screen.fill(white)

current_sort_index = 0
pygame.display.set_caption(f"{sort_names[current_sort_index]} Sort")

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

make_board()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F5:
                print("Resetting Board")
                make_board()
                print("Board Reset")
            if event.key == pygame.K_RETURN:
                print("Sorting")
                sorts[current_sort_index]()
                print("Sorted")
            if event.key == pygame.K_RIGHT:
                change_sort("next")
            if event.key == pygame.K_LEFT:
                change_sort("back")
            if event.key == pygame.K_s:
                step_show = not step_show
                step_time = default_step_time if step_show else 0
                print(f"Showing steps is {step_show}")
