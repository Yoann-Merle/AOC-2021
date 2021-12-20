#!/bin/python3
import numpy as np
import re
import copy
import time

def read_input():
    filename = 'input-test.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def run_algo(algo, seq):
    seq = seq.replace('.','0')
    seq = seq.replace('#','1')
    return algo[int(seq, 2)]

def enhance(image, algo, fill = '.'):
    new_image = []
    for y in range(-1, len(image) + 1):
        new_line = []
        for x in range(-1, len(image[0]) + 1):
            seq = ''
            for y_ in range(y-1, y+2):
                for x_ in range(x-1, x+2):
                    if y_ < 0 or x_ < 0 or y_ >= len(image) or x_ >= len(image[0]):
                        seq += fill
                    else:
                        seq += image[y_][x_]
            new_point = run_algo(algo, seq)
            new_line.append(new_point)
        new_image.append(new_line)
    return new_image


def print_image(image):
    for l in image:
        print(''.join(l))
    print()

def count_white_pixels(image):
    count = 0
    for y in range(len(image)):
        for x in range(len(image[y])):
            if image[y][x] == '#':
                count += 1
    return count

def main():
    start = time.time()
    lines = read_input()
    algo = [x for x in lines[0]]
    image = []
    for line in lines[2:]:
        image.append([x for x in line])


    # Star 1
    fill = '.'
    for i in range(50):
        if algo[0] == '#' and algo[-1] == '.':
            fill = '.' if i % 2 == 0 else '#'
        image = enhance(image, algo, fill)
        if i == 1:
            print('Start 1: ', count_white_pixels(image))
            end = time.time()
            print('Execution time %3.1f s' %(end - start))
        if i == 49:
            print('Start 2: ', count_white_pixels(image))
            end = time.time()
            print('Execution time %3.1f s' %(end - start))
        print_image(image)
main()
