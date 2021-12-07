#!/bin/python3
import numpy as np
import copy

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def calculate_diff(val, serie):
    sum_diff = 0
    for v in serie:
        sum_diff += abs(v - val)

    return sum_diff

def calculate_diff_2(val, serie):
    sum_diff = 0
    for v in serie:
        sum_diff += sum([i + 1 for i, a in enumerate(range(abs(v - val)))])

    return sum_diff

def main():
    lines = read_file('input.txt')
    crabs = [int(a) for a in lines[0].split(',')]
    min = np.min(crabs)
    max = np.max(crabs)

    # part 1
    diff = {}
    for i in range(min, max):
        diff[i] = calculate_diff(i, crabs)

    print('Start 1: ', np.min(list(diff.values())))

    # part 2
    diff = {}
    for i in range(min, max):
        diff[i] = calculate_diff_2(i, crabs)

    print('Start 2: ', np.min(list(diff.values())))

main()
