#!/bin/python3
import numpy as np
import copy

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def polymerize(seq, rules):
    seq_copy = copy.copy(seq)
    for i, v in enumerate(seq_copy):
        if i == len(seq_copy) - 1:
            break
        j = 1 + (i * 2)
        ins = rules[seq[j - 1] + seq[j]]
        seq = seq[:j] + [ins] + seq[j:]
    return seq

def update_parents(rr, parents):
    new_parents = {}
    for child in parents:
        if len(child) == 1:
            new_parents[child] = new_parents[child] + parents[child] if child in new_parents else parents[child]
            for p in rr[child]:
                new_parents[p] = new_parents[p] + parents[child] if p in new_parents else parents[child]
        else:
            for p in rr[child[0]]:
                if p[1] == child[1]:
                        new_parents[p] = new_parents[p] + parents[child] if p in new_parents else parents[child]
            for p in rr[child[1]]:
                if p[0] == child[0]:
                        new_parents[p] = new_parents[p] + parents[child] if p in new_parents else parents[child]
    return new_parents


def calculate_score(seq):
    uniq_seq = set(seq)
    max_el = 0
    min_el = len(seq)
    for el in uniq_seq:
        nb = seq.count(el)
        max_el = nb if nb > max_el else max_el
        min_el = nb if nb < min_el else min_el
    return max_el - min_el

def main():
    lines = read_file('input.txt')
    seq_ = [x for x in lines[0]]
    rules = {}
    reverse_rules = {}
    for line in lines[2:]:
        key, sep, val = line.split()
        rules[key] = val
    for key in rules:
        if rules[key] in reverse_rules:
            reverse_rules[rules[key]].append(key)
        else:
            reverse_rules[rules[key]] = [key]

    # Star 1
    seq = copy.copy(seq_)
    for i in range(10):
        seq = polymerize(seq, rules)
    print('Star 1', calculate_score(seq))


    # Star 2
    total = {}
    seq = copy.copy(seq_)
    for l in set(''.join(rules.keys())):
        parents = {}
        parents[l] = 1
        for i in range(40):
            parents = update_parents(reverse_rules, parents)
            total[l] = 0
            for j in range(len(seq)):
                u = seq[j]
                if u in parents:
                    total[l] += parents[u]
                if j < len(seq) - 1:
                    d = seq[j] + seq[j+1]
                    if d in parents:
                        total[l] += parents[d]
    max_el = 0
    min_el = 1000000000000000000000000000000000
    for el in total:
        max_el = total[el] if total[el] > max_el else max_el
        min_el = total[el] if total[el] < min_el else min_el

    print('Start 2: ', max_el - min_el)



main()
