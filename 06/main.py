#!/bin/python3
import numpy as np
import copy

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def defineOrderedArray(array_origin, origin_length):
    id_array = [0 for a in range(origin_length)]
    for el in array_origin:
        id_array[el] += 1

    return id_array

def life_cycle(fishes, days):
    nb_fishes_7 = 0
    nb_fishes_8 = 0
    for day in range(days):
        fishes = np.roll(fishes, - 1)
        new_fishes = fishes[6]
        fishes[6] += nb_fishes_7
        nb_fishes_7 = nb_fishes_8
        nb_fishes_8 = new_fishes
    return sum(fishes) + nb_fishes_7 + nb_fishes_8

def main():
    lines = read_file('input.txt')
    fishes = defineOrderedArray([int(a) for a in lines[0].split(',')], 7)

    # part 1
    fishes_clone = fishes.copy()
    final_pop = life_cycle(fishes_clone, 80)
    print('Start 1: ', final_pop)

    # part 2
    fishes_clone = fishes.copy()
    final_pop = life_cycle(fishes_clone, 256)
    print('Start 2: ', final_pop)

main()
