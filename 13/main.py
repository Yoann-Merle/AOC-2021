#!/bin/python3
import numpy as np
import copy

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def fold(matrice, instruc):
    axe = instruc[0]
    fold_nb = instruc[1]
    for dot in copy.copy(matrice):
        if axe == 'x' and dot[0] < fold_nb:
            matrice.add((fold_nb * 2 - dot[0], dot[1]))
            matrice.remove((dot[0], dot[1]))
        if axe == 'y' and dot[1] > fold_nb:
            matrice.add((dot[0], fold_nb * 2 - dot[1]))
            matrice.remove((dot[0], dot[1]))
    for dot in copy.copy(matrice):
        if axe == 'x':
            matrice.remove(dot)
            matrice.add((dot[0] - fold_nb - 1, dot[1]))

def print_matrice(m):
    max_x = 0
    max_y = 0
    for p in m:
        max_x = p[0] if p[0] > max_x else max_x
        max_y = p[1] if p[1] > max_y else max_y
    for y in range(max_y + 1):
        line = ''
        for x in range(max_x + 1):
            c = '#' if (x, y) in m else '.'
            line = c + line # Don't know why but need to reverse
        print(line)

def main():
    lines = read_file('input.txt')
    matrice = set()
    fold_instruct = []
    dots = True
    for line in lines:
        if line == '':
            dots = False
            continue
        if dots:
            x, y = [int(x) for x in line.split(',')]
            matrice.add((x, y))
        else:
            axe, nb = line.split()[2].split('=')
            fold_instruct.append((axe, int(nb)))

    # Star 1
    fold(matrice, fold_instruct[0])
    print('Start 1: ', len(matrice))

    # Star 2
    for inst in fold_instruct[1:]:
        fold(matrice, inst)
    print('Start 2: ')
    print_matrice(matrice)



main()
