#!/bin/python3
import numpy as np
import copy

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def complete_path(path, caves):
    c_paths = []
    for cave in caves:
        copy_path = copy.copy(path)
        if path[-1] in cave:
            i = 1 if path[-1] == cave[0] else 0
            if cave[i].isupper() or (cave[i].islower() and cave[i] not in path):
                copy_path.append(cave[i])
                c_paths.append(copy_path)

    return c_paths

def clean_paths(paths):
    finished_paths = []
    for path in copy.copy(paths):
        if path[-1] == 'end':
            finished_paths.append(path)
            paths.remove(path)
    return finished_paths

def main():
    lines = read_file('input.txt')
    caves = []
    paths = []
    f_paths = []
    for line in lines:
        x, y = line.split('-')
        if x == 'start':
            paths.append([x, y])
            continue
        if y == 'start':
            paths.append([y, x])
            continue
        caves.append((x, y))

    while len(paths) > 0:
        f_paths += clean_paths(paths)
        for path in copy.copy(paths):
            c_paths = complete_path(path, caves)
            paths += c_paths
            paths.remove(path)

    # Star 1
    print('Start 1: ', len(f_paths))

main()
