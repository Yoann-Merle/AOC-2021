#!/bin/python3
import numpy as np
import copy

delimiters = {
        ')': {'open': False, 'price': 3, 'cprice': 1, 'meet': '('},
        '(': {'open': True, 'price': 3, 'cprice': 1, 'meet': ')'},
        ']': {'open': False, 'price': 57, 'cprice': 2, 'meet': '['},
        '[': {'open': True, 'price': 57, 'cprice': 2, 'meet': ']'},
        '}': {'open': False, 'price': 1197, 'cprice': 3, 'meet': '{'},
        '{': {'open': True, 'price': 1197, 'cprice': 3, 'meet': '}'},
        '>': {'open': False, 'price': 25137, 'cprice': 4, 'meet': '<'},
        '<': {'open': True, 'price': 25137, 'cprice': 4, 'meet': '>'},
}

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def score(line):
    open_char = []
    for c in line:
        if delimiters[c]['open'] == True:
            open_char.append(c)
        else:
            c_ = open_char.pop()
            if delimiters[c]['meet'] != c_:
                return True, delimiters[c]['price']
    score = 0
    for oc in open_char[::-1]:
        score *= 5
        score += delimiters[oc]['cprice']

    return False, score

def main():
    lines = read_file('input.txt')

    corr_prices = 0
    incomplete_scores = []
    incomplete_lines = []
    for line in lines:
        corr, price = score(line)
        if corr:
            corr_prices += price
        else:
            incomplete_scores.append(price)

    print('Start 1: ', corr_prices)
    print('Start 2: ', sorted(incomplete_scores)[int(len(incomplete_scores)/2)])

main()
