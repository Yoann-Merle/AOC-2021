#!/bin/python3
import numpy as np
import re
import copy
import time

def read_input():
    filename = 'input.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def next(point, v):
    point[0] += v[0]
    point[1] += v[1]
    if v[0] != 0:
        v[0] = v[0] - 1 if v[0] > 0 else v[0] + 1
    v[1] -= 1
    return point, v

def launch(point, v, limits):
    max_y = point[1]
    while True:
        point, v = next(point, v)
        max_y = point[1] if point[1] > max_y else max_y
        if point[0] > limits[0][1]:
            return [1, 0], max_y
        if point[0] < limits[0][0] and v[0] == 0:
            return [-1, 0], max_y
        if point[1] < limits[1][0]:
            return [0, 1], max_y
        if point[0] <= limits[0][1] and point[0] >= limits[0][0] \
            and point[1] <= limits[1][1] and point[1] >= limits[1][0]:
            return [0, 0], max_y

def main():
    start = time.time()
    lines = read_input()
    x_min, x_max, y_min, y_max = re.findall("(-*\d+)", lines[0])
    limits = [[int(x_min), int(x_max)], [int(y_min), int(y_max)]]

    # Star 1
    p = [0, 0]
    v = [1, 1000]
    max = None
    while True:
        corr, max_y = launch(copy.copy(p), copy.copy(v), limits)
        if corr[0] == 0 and corr[1] == 0:
            max = max_y
            break
        v[0] -= corr[0]
        v[1] -= corr[1]


    print('Start 1: ', max_y)
    end = time.time()
    print('Execution time %3.1f s' %(end - start))

    # Star 2
    p = [0, 0]
    collect_v = set()
    for x in range(-300, 300):
        for y in range(-300, 300):
            corr, max_y = launch(copy.copy(p), [x, y], limits)
            if corr[0] == 0 and corr[1] == 0:
                collect_v.add((x, y))

    print('Start 2: ', len(collect_v))
    end = time.time()
    print('Execution time %3.1f s' %(end - start))

main()
