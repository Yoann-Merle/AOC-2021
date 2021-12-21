#!/bin/python3
import numpy as np
import re
import copy
import time

def read_input():
    filename = 'input.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def roll(dice):
    sum = 0
    for i in range(3):
        sum += dice + 1
        dice += 1
        dice %= 100
    return sum

def quantic_roll(dice):
    pos = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                pos.append(i + j + k + 3)
    return pos

def clean_high_scores(ps, p):
    psc = copy.copy(ps[p])
    psc2 = copy.copy(ps[1]) if p == 0 else copy.copy(ps[0])
    loser_count = 0
    for s in psc2:
        if s < 21:
            for pos in psc2[s]:
                loser_count += psc2[s][pos]

    count = 0
    for s in psc:
        if s >= 21:
            for pos in psc[s]:
                count += psc[s][pos] * loser_count
            ps[p].pop(s)
    return ps, count

def main():
    start = time.time()
    lines = read_input()
    playersPosition = [int(lines[0].split()[-1]) - 1, int(lines[1].split()[-1]) - 1]

    # Star 1
    dice = 0
    playersScore = [0, 0]
    playerTurn = 0
    nbRolls = 0
    playersPos = copy.copy(playersPosition)
    while True:
        nbRolls += 3
        nb = roll(dice)
        dice = (dice + 3) % 100
        playersPos[playerTurn] = (playersPos[playerTurn] + nb) % 10
        playersScore[playerTurn] += playersPos[playerTurn] + 1
        if playersScore[playerTurn] >= 1000:
            break
        playerTurn += 1
        playerTurn %= 2

    print('Start 1: ', nbRolls * playersScore[(playerTurn + 1)%2])
    end = time.time()
    print('Execution time %3.1f s' %(end - start))


    # star 2
    playerTurn = 0
    playersPos = copy.copy(playersPosition)
    pos_and_score = [{0: {playersPos[0]: 1}}, {0: {playersPos[1]: 1}}]
    victories = [0, 0]
    i = 0
    while len(pos_and_score[0]) > 0 or len(pos_and_score[1]) > 0:
        nb = quantic_roll(dice)
        new_pos_and_score = {}
        for old_score in pos_and_score[playerTurn]:
            for old_pos in pos_and_score[playerTurn][old_score]:
                old_count = pos_and_score[playerTurn][old_score][old_pos]
                for n in set(nb):
                    new_count = nb.count(n)
                    new_pos = (old_pos + n) % 10
                    new_score = old_score + new_pos + 1
                    if new_score not in new_pos_and_score:
                        new_pos_and_score[new_score] = {new_pos: old_count * new_count}
                    else:
                        if new_pos in new_pos_and_score[new_score]:
                            new_pos_and_score[new_score][new_pos] += old_count * new_count
                        else:
                            new_pos_and_score[new_score][new_pos] = old_count * new_count

        pos_and_score[playerTurn] = new_pos_and_score
        pos_and_score, c = clean_high_scores(pos_and_score, playerTurn)
        victories[playerTurn] += c

        playerTurn += 1
        playerTurn %= 2

    print('Start 2: ', np.max(victories))
    end = time.time()
    print('Execution time %3.1f s' %(end - start))
main()
