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
        point = start
        if end not in points:
            points[end] = 0
        points[end] += 1
        while point != end:
            if point not in points:
                points[point] = 0
            points[point] += 1
            if point[0] < end[0]:
                point = (point[0] + 1, point[1])
            if point[0] > end[0]:
                point = (point[0] - 1, point[1])
            if point[1] < end[1]:
                point = (point[0], point[1] + 1)
            if point[1] > end[1]:
                point = (point[0], point[1] - 1)

    return points

def main():
    lines = read_file('input.txt')

    # part 1
    seg = extract_segments(lines)
    points = generate_points(seg)
    nb_multi_points = sum([1 for x in points if points[x] > 1])
    print('Start 1: ', sum([1 for x in points if points[x] > 1]))

    # part 2
    seg = extract_segments(lines, False)
    points = generate_points(seg)

    print('Start 2: ', sum([1 for x in points if points[x] > 1]))

main()
