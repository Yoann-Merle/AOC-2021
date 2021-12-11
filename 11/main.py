#!/bin/python3
import numpy as np
import copy

adjacent = [
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 0),
        (0, 0),
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
]

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def flash(grid, x, y):
    for a in adjacent:
        x_ = x + a[0]
        y_ = y + a[1]
        if x_ >= 0 and y_ >= 0 and y_ < len(grid) and x_ < len(grid[y_]):
            grid[y_][x_] += 1

def calc_flashes(grid):
    flashes_nb = 0
    flashes_set = set()
    # step 1
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid[y][x] += 1

    # step 2
    has_flashed = True
    while has_flashed:
        has_flashed = False
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] > 9 and (x, y) not in flashes_set:
                    has_flashed = True
                    flashes_set.add((x, y))
                    flash(grid, x, y)
                    flashes_nb += 1

    # step 3
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] > 9:
                grid[y][x] = 0

    return flashes_nb

def all_zero(grid):
   for y in range(len(grid)):
       for x in range(len(grid[y])):
           if grid[y][x] != 0:
               return False
   return True

def main():
    lines = read_file('input.txt')
    octopus_grid = []
    for line in lines:
        octopus_grid.append([int(o) for o in line])

    # Star 1 & star 2
    flashes_nb = 0
    og = copy.copy(octopus_grid)
    for step in range(10000):
        flashes_nb += calc_flashes(og)
        if (step + 1 == 100):
            print('Start 1: ', flashes_nb)
        if all_zero(og):
            print('Start 2: ', step + 1)
            return


main()
