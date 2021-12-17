#!/bin/python3
import numpy as np
import copy
import time

def read_input():
    filename = 'input.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def get_type_version(seq):
    return int(seq[:3], 2), int(seq[3:6], 2)

def get_literal_v(seq):
    i = 0
    v = ''
    while True:
        v += seq[i+1:i+5]
        i += 5
        if seq[i-5] == '0':
            break

    return int(v, 2), i

def sum_version(packets):
    sum_ = 0
    for p in packets:
        sum_ += p['version']
        if p['type'] != 4:
            sum_ += sum_version(p['content'])

    return sum_

def calcul_packets(packets):
    values = []
    for p in packets:
        if p['type'] == 4:
            values.append(p['content'])
            continue
        sub_packets = calcul_packets(p['content'])
        v = None
        if p['type'] == 0:
            v = 0
            v = np.sum(sub_packets)
        if p['type'] == 1:
            v = np.prod(sub_packets)
        if p['type'] == 2:
            v = np.min(sub_packets)
        if p['type'] == 3:
            v = np.max(sub_packets)
        if p['type'] == 5:
            v = 1 if sub_packets[0] > sub_packets[1] else 0
        if p['type'] == 6:
            v = 1 if sub_packets[0] < sub_packets[1] else 0
        if p['type'] == 7:
            v = 1 if sub_packets[0] == sub_packets[1] else 0
        values.append(v)
    return values

def get_packets(seq, j, c = -1):
    packets = []
    index = 0
    while c != 0 and index < len(seq) - 6:
        version, type_ = get_type_version(seq[index:])
        index += 6
        if type_ == 4:
            lv, i = get_literal_v(seq[index:])
            index += i
            packets.append({'version': version, 'type': type_, 'content': lv})
        else:
            length_value = 15 if seq[index] == '0' else 11
            index += 1
            length = int(seq[index:index + length_value], 2)
            index += length_value
            inside_packets = []
            if length_value == 15:
                inside_packets, _ = get_packets(seq[index:index + length + 1], j + 1)
                index += length
            else:
                inside_packets, new_length = get_packets(seq[index:], j + 1, length)
                index += new_length
            packets.append({'version': version, 'type': type_, 'content': inside_packets})
        c -= 1

    return packets, index

def main():
    start = time.time()
    lines = read_input()
    hexa_sequence = lines[0]
    bin_sequence = ''.join([format(int(hexa_s, 16), '04b') for hexa_s in hexa_sequence])

    packets, _ = get_packets(bin_sequence, 0, 1)
    # Star 1
    print('Start 1: ', sum_version(packets))
    end = time.time()
    print('Execution time %3.1f s' %(end - start))

    # Star 2
    print('Start 2: ',calcul_packets(packets))
    end = time.time()
    print('Execution time %3.1f s' %(end - start))

main()
