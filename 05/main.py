#!/bin/python3
import copy

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def extract_segments(lines, filter=True):
    segments = []
    for line in lines:
        start, end = line.split(' -> ')
        start_x, start_y = map(int, start.split(','))
        end_x, end_y = map(int, end.split(','))
        if filter == True and start_x != end_x and start_y != end_y:
            continue
        segments.append(((start_x, start_y), (end_x, end_y)))
    return segments

def generate_points(segments):
    points = {}
    for segment in segments:
        start = segment[0]
        end = segment[1]
        if start[0] == end[0]:
            if start[1] > end[1]:
                for p in range(end[1], start[1] + 1):
                    if (start[0], p) not in points:
                        points[(start[0], p)] = 0
                    points[(start[0], p)] += 1
            else:
                for p in range(start[1], end[1] + 1):
                    if (start[0], p) not in points:
                        points[(start[0], p)] = 0
                    points[(start[0], p)] += 1
        else:
            if start[0] > end[0]:
                for p in range(end[0], start[0] + 1):
                    if (p, start[1]) not in points:
                        points[(p, start[1])] = 0
                    points[(p, start[1])] += 1
            else:
                for p in range(start[0], end[0] + 1):
                    if (p, start[1]) not in points:
                        points[(p, start[1])] = 0
                    points[(p, start[1])] += 1
    return points

def main():
    lines = read_file('input.txt')
    seg = extract_segments(lines)
    points = generate_points(seg)
    nb_multi_points = sum([1 for x in points if points[x] > 1])
    print('Start 1: ', nb_multi_points)

    # print('Start 2: ', result)


main()
