#!/bin/python3
import numpy as np
import copy
import time

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def extend_path(p, m, clone):
    last_point = p['lp']
    extensions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    dims = (len(m[0]), len(m)) if not clone else (len(m[0]) * 5, len(m) * 5)
    new_paths = []
    for ext in extensions:
        next_point = (ext[0] + last_point[0], ext[1] + last_point[1])
        if next_point[0] < 0 or next_point[1] < 0 \
                or next_point[0] >= dims[0] or next_point[1] >= dims[1]:
            continue
        if next_point in p['path']:
            continue
        x_factor = int(next_point[0] / len(m[0]))
        x_delta = next_point[0] % len(m[0])
        y_factor = int(next_point[1] / len(m))
        y_delta = next_point[1] % len(m)
        score = (m[x_delta][y_delta] + y_factor + x_factor)
        if score >= 10:
            score %= 9
        new_path = {'path': copy.copy(p['path']), 'lp': next_point, 'score': p['score'] + score}
        new_path['path'].add(next_point)
        new_paths.append(new_path)

    return new_paths

def find_success_paths(map_, clone = False):
    paths = [{'path': set(), 'lp': (0, 0), 'score': 0}]
    paths[0]['path'].add((0, 0))
    min_scores = {}
    success_paths = []
    while len(paths) > 0:
        gen_paths = []
        for path in paths:
            gen_paths += extend_path(path, map_, clone)
        paths = []
        garbage_coll = {}
        for gen_path in gen_paths:
            last_el = gen_path['lp']
            score = gen_path['score']
            if last_el not in min_scores:
                min_scores[last_el] = score
            else:
                if score >= min_scores[last_el]:
                    continue
            min_scores[last_el] = score
            garbage_coll[last_el] = score
            paths += [gen_path]
            if (not clone and last_el == (len(map_[0]) - 1, len(map_) - 1)) or \
                (clone and last_el == (len(map_[0]) * 5 - 1, len(map_) * 5 - 1)):
                success_paths += [gen_path]

        copy_paths = copy.copy(paths)
        paths = []
        for path in copy_paths:
            keep = True
            for key in garbage_coll:
                if key == path['lp'] and path['score'] > garbage_coll[key]:
                    keep = False
                    break
            if keep:
                paths += [path]
        print(len(paths))

    return success_paths

def main():
    lines = read_file('input.txt')
    map_ = []
    dim = []
    for line in lines:
        map_.append([int(x) for x in line])

    # Star 1
    success_paths = find_success_paths(map_)
    min_score = None
    min_sp = None
    for sp in success_paths:
        if min_score == None or min_score > sp['score']:
            min_score = sp['score']
            min_sp = sp
    print('Start 1: ', min_score)

    # Star 2
    success_paths = find_success_paths(map_, True)
    min_score = None
    min_sp = None
    for sp in success_paths:
        if min_score == None or min_score > sp['score']:
            min_score = sp['score']
            min_sp = sp
    print('Start 2: ', min_score)
    # There is much simpler : keep score on every point (no need to keep paths)

main()
