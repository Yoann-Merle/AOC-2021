#!/bin/python3

def read_file(filename):
    f = open(filename)
    lines = f.readlines()
    return lines

def sum_array(array):
    sum = 0
    for i in array:
        sum += i
    return sum

def main():
    increase_count = 0
    lines = read_file('input.txt')
    # part 1
    previousLine = None
    for line in lines:
        int_line = int(line)
        if previousLine is not None:
            if previousLine < int_line:
                increase_count += 1
        previousLine = int_line

    print(increase_count)

    # part 2
    increase_count = 0
    previousGroup = [int(line[0]), int(line[1]), int(line[2])]
    for line in lines[3:]:
        int_line = int(line)
        currentGroup = previousGroup[1:] + [int_line]
        if sum_array(previousGroup) < sum_array(currentGroup):
            increase_count += 1
        previousGroup = currentGroup

    print(increase_count)

main()
