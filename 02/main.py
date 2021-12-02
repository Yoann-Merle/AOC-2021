#!/bin/python3
import re

def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()

    return lines

def move(pos, line):
    extract = re.findall(r'([a-zA-Z]*)\s(\d)', line)[0]
    key = extract[0]
    val = int(extract[1])
    x, y = pos
    if key == 'forward':
        return (x + val, y)
    if key == 'down':
        return (x, y + val)
    if key == 'up':
        return (x, y - val)
    raise Exception('Regex condition not met')

def move2(pos, aim, line):
    extract = re.findall(r'([a-zA-Z]*)\s(\d)', line)[0]
    key = extract[0]
    val = int(extract[1])
    if key == 'forward':
        x, y = pos
        return ((x + val, y + aim * val), aim)
    if key == 'down':
        return (pos, aim + val)
    if key == 'up':
        return (pos, aim - val)
    raise Exception('Regex condition not met')


def main():
    increase_count = 0
    lines = read_file('input.txt')

    # part 1
    x = 0
    y = 0
    for line in lines:
        x, y = move((x, y), line)

    print (x * y)

    #part 2
    x = 0
    y = 0
    aim = 0
    for line in lines:
        (x, y), aim = move2((x, y), aim, line)

    print (x * y)

main()
