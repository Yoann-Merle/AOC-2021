#!/bin/python3
import copy

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def split(lines, index):
    lines_1 = []
    lines_0 = []
    for line in lines:
        if line[index] == '1':
            lines_1 += [line]
        else:
            lines_0 += [line]
    return (lines_0, lines_1)

def main():
    lines = read_file('input.txt')
    total = len(lines)

    # part 1
    count = []
    for ind, line in enumerate(lines):
        if ind == 0:
            count = [0 for col in range(len(line))]
        for i, x in enumerate(line):
            if x == '1':
                count[i] += 1

    gammaRateBin = ''
    for x in range(len(count)):
        if count[x] > int(total / 2):
            gammaRateBin += '1'
        else:
            gammaRateBin += '0'
    gammaRateNum = int(gammaRateBin, 2)
    epsilonRateNum = gammaRateNum ^ int('1' * len(count), 2)

    print('Start 1: ', gammaRateNum * epsilonRateNum)

    # part 2
    oxyGenSubSet = copy.deepcopy(lines)
    CO2ScrubSubSet = copy.deepcopy(lines)
    i = 0
    while len(oxyGenSubSet) > 1:
        list0, list1 = split(oxyGenSubSet, i)
        if len(list1) >= len(list0):
            oxyGenSubSet = copy.deepcopy(list1)
        else:
            oxyGenSubSet = copy.deepcopy(list0)
        i += 1

    i = 0
    while len(CO2ScrubSubSet) > 1:
        list0, list1 = split(CO2ScrubSubSet, i)
        if len(list1) >= len(list0):
            CO2ScrubSubSet = copy.deepcopy(list0)
        else:
            CO2ScrubSubSet = copy.deepcopy(list1)
        i += 1

    CO2ScrubInt = int(CO2ScrubSubSet[0], 2)
    oxyGenInt = int(oxyGenSubSet[0], 2)

    print('Start 2: ', CO2ScrubInt * oxyGenInt)


main()
