#!/bin/python3
import numpy as np
import copy


def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def calculate_bassin(carto, x, y):
    search_points = set()
    search_points.add((int(x), int(y)))
    all_points = set()
    while len(search_points) > 0:
        all_points = all_points.union(search_points)
        search_point_add = set()
        for x, y in search_points.copy():
            if x - 1 >= 0 and carto[y][x - 1] != 9:
                if (x-1, y) not in all_points:
                    search_point_add.add((x-1, y))
            if x + 1 < len(carto[y]) and carto[y][x + 1] != 9:
                if (x+1, y) not in all_points:
                    search_point_add.add((x+1, y))
            if y - 1 >= 0 and carto[y-1][x] != 9:
                if (x, y-1) not in all_points:
                    search_point_add.add((x, y-1))
            if y + 1 < len(carto) and carto[y+1][x] != 9:
                if (x, y+1) not in all_points:
                    search_point_add.add((x, y+1))
        search_points = search_point_add


    return len(all_points)

def main():
    lines = read_file('input.txt')
    carto = []
    for line in lines:
        carto.append([int(x) for x in line])

    # part 1
    lowest_points = []
    for y, line in enumerate(carto):
        for x, v in enumerate(line):
            if x - 1 >= 0 and carto[y][x - 1] <= carto[y][x]:
                continue
            if x + 1 < len(line) and carto[y][x + 1] <= carto[y][x]:
                continue
            if y - 1 >= 0 and carto[y-1][x] <= carto[y][x]:
                continue
            if y + 1 < len(carto) and carto[y +1][x] <= carto[y][x]:
                continue
            lowest_points.append((x, y, v))

    print('Start 1: ', sum([ v + 1 for x, y, v in lowest_points]))


    # part 2
    bassins_size = []
    for x, y, v in lowest_points:
        bassins_size.append(calculate_bassin(carto, x, y))
        if len(bassins_size) > 3:
            bassins_size.remove(min(bassins_size))

    print('Start 2: ', bassins_size[0] * bassins_size[1] * bassins_size[2])

main()
