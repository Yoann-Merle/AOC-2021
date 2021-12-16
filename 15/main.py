#!/bin/python3
import numpy as np
import copy
import time

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def extend_point(p, m, min_scores, clone):
    extensions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    dims = (len(m[0]), len(m)) if not clone else (len(m[0]) * 5, len(m) * 5)
    new_points = []
    for ext in extensions:
        next_point = (ext[0] + p[0], ext[1] + p[1])
        if next_point[0] < 0 or next_point[1] < 0 \
                or next_point[0] >= dims[0] or next_point[1] >= dims[1]:
            continue
        x_factor = int(next_point[0] / len(m[0]))
        x_delta = next_point[0] % len(m[0])
        y_factor = int(next_point[1] / len(m))
        y_delta = next_point[1] % len(m)
        score = (m[x_delta][y_delta] + y_factor + x_factor)
        if score >= 10:
            score %= 9
        next_score = score + min_scores[p]
        if next_point in min_scores and min_scores[next_point] <= next_score:
            continue
        min_scores[next_point] = next_score
        new_points.append(next_point)

    return new_points

def find_best_score(map_, clone = False):
    used_points = set()
    init_point = (0, 0)
    points = set()
    points.add(init_point)
    min_scores = {(0, 0): 0}

    while len(points) > 0:
        np = []
        for p in points:
            np += extend_point(p, map_, min_scores, clone)
        points = np
    return min_scores

def main():
    lines = read_file('input.txt')
    map_ = []
    dim = []
    for line in lines:
        map_.append([int(x) for x in line])

    # Star 1
    scores = find_best_score(map_)
    print('Start 1: ', scores[(len(map_[0]) - 1, len(map_) - 1)])

    # Star 2
    scores = find_best_score(map_, True)
    print('Start 2: ', scores[(len(map_[0]) * 5 - 1, len(map_) * 5 - 1)])

main()
