#!/bin/python3
import copy

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def split_by_empty_line(lines):
    blocks = []
    noted = []
    for line in lines:
        if line == '':
            blocks.append([])
            noted.append([])
        else:
            blocks[len(blocks) - 1].append(line.split())
            noted[len(blocks) - 1].append([0 for a in line.split()])

    return blocks, noted

def board_complete(noted_board, line_nb, col_nb):
    line_complete = True
    col_complete = True
    for nb in noted_board[line_nb]:
        if nb == 0:
            line_complete = False
            break
    for nb in range(len(noted_board)):
        if noted_board[nb][col_nb] == 0:
            col_complete = False
            break
    return line_complete or col_complete

def sum_score(board, noted):
    sum = 0
    for l, line_noted in enumerate(noted):
        for n, nb in enumerate(line_noted):
            if nb == 0:
                sum += int(board[l][n])
    return sum

def play(boards, noted, drawn_nb):
    for nb in drawn_nb:
        for b, board in enumerate(boards):
            for l, line in enumerate(board):
                for c, char in enumerate(line):
                    if char == nb:
                        noted[b][l][c] = 1
                        if board_complete(noted[b], l, c):
                            return int(nb) * sum_score(board, noted[b]), b

def main():
    lines = read_file('input.txt')
    drawn_nb = [ a for a in lines[0].split(',')]
    boards, noted = split_by_empty_line(lines[1:])
    noted_copy = copy.deepcopy(noted)
    result, _ = play(boards, noted, drawn_nb)
    print('Start 1: ', result)

    boards_copy = copy.deepcopy(boards)
    while (len(boards_copy) > 0):
        result, index = play(boards_copy, noted_copy, drawn_nb)
        boards_copy.pop(index)
        noted_copy.pop(index)
    print('Start 2: ', result)


main()
