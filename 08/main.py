#!/bin/python3
import numpy as np
import copy

all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
numbers = {
        1: {'c', 'f'},
        7: {'a', 'c', 'f'},
        4: {'b', 'c', 'd', 'f'},
        2: {'a', 'c', 'd', 'e', 'g'},
        3: {'a', 'c', 'd', 'f', 'g'},
        5: {'a', 'b', 'd', 'f', 'g'},
        9: {'a', 'b', 'c', 'd', 'f', 'g'},
        0: {'a', 'b', 'c', 'e', 'f', 'g'},
        6: {'a', 'b', 'd', 'e', 'f', 'g'},
        8: {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    }

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def find_number(rw, signal, count_repet):
    filtered_numbers = [n for n in numbers if len(numbers[n]) == len(signal)]
    final_numbers = set()
    for n in filtered_numbers:
        exclude = False
        for l in signal:
            possible_letters = [a for a in all_letters if a not in rw[l]]
            result = list(filter(lambda x: x in possible_letters, numbers[n]))
            if len(result) == 0:
                exclude = True
        if exclude == False:
            final_numbers.add(n)

    if len(final_numbers) == 1:
        return list(final_numbers)[0]
    return -1

def reduce_possible(rw, signal, count_repet):
    nb = find_number(rw, signal, count_repet)
    if nb == -1:
        return
    not_in_set = [a for a in all_letters if a not in signal]
    in_output = list(numbers[nb])
    not_in_output = [a for a in all_letters if a not in in_output]
    for l in signal:
        if count_repet[l] != 9:
            rw[l].add('f')
        if count_repet[l] != 6:
            rw[l].add('b')

    for l in not_in_set:
        for r in in_output:
            rw[l].add(r)

    for l in signal:
        for r in not_in_output:
            rw[l].add(r)


def main():
    lines = read_file('input.txt')
    entries = []
    for line in lines:
        signals = line.split('|')[0].split()
        output_values = line.split('|')[1].split()
        entries.append([signals, output_values])

    # part 1
    uniq_count = 0
    for entrie in entries:
        for output_value in entrie[1]:
            if len(output_value) in (2, 3, 4, 7):
                uniq_count += 1

    print('Start 1: ', uniq_count)

    # part 2
    sum_entries = 0
    for entrie in entries:
        reverse_wiring = {'a': set(), 'b': set(), 'c': set(), 'd': set(), 'e': set(), 'f': set(), 'g': set()}
        count_repet = {}
        for letter in all_letters:
            count_repet[letter] = ''.join(entrie[0]).count(letter)
        while True:
            for signal in entrie[0]:
                reduce_possible(reverse_wiring, signal, count_repet)

            if sum([1 for a in reverse_wiring.values() if len(a) != 6]) == 0:
                output = ''
                for n in entrie[1]:
                    num = find_number(reverse_wiring, n, count_repet)
                    output += str(num)

                sum_entries += int(output)
                break

    print('Start 2: ', sum_entries)

main()
