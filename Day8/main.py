import copy
from collections import defaultdict

import numpy as np


def get_input():
    with open("input.txt") as f:
        data = f.read()
        data_splitted = data.split("\n")
        to_grid = []
        for row in data_splitted:
            to_grid.append(list(row))
    return to_grid


def draw_antinodes(a, b, antenna_grid, pt2=False):
    p1 = np.array(a)
    p2 = np.array(b)
    d = np.linalg.norm(p2 - p1)

    direction = p2 - p1

    unit_vector = direction / np.linalg.norm(direction)
    new_p2 = p1 - unit_vector * d

    antinode_counter = 0
    if pt2:
        while 0 <= new_p2[0] < len(antenna_grid) and 0 <= new_p2[1] < len(antenna_grid[0]):
            x = round(new_p2[0])  # Round before casting to int
            y = round(new_p2[1])  # Round before casting to int
            if antenna_grid[x][y] == "." and not antenna_grid[x][y] == "#":
                antinode_counter += 1
                antenna_grid[x][y] = "#"

            # Update new_p2 to one step further
            new_p2 = new_p2 - unit_vector * d
    else:
        x = int(new_p2[0])
        y = int(new_p2[1])
        if 0 <= x < len(antenna_grid) and 0 <= y < len(antenna_grid[0]):
            if antenna_grid[int(x)][int(y)] == "." or not antenna_grid[x][
                                                              y] == "#":
                antinode_counter += 1
                antenna_grid[x][y] = "#"

    return antinode_counter


def get_antennas(antenna_grid):
    antennas = defaultdict(list)

    for i in range(len(antenna_grid)):
        for j in range(len(antenna_grid[i])):
            if antenna_grid[i][j] != ".":
                antennas[antenna_grid[i][j]].append((i, j))
    return antennas


def part1(data):
    antenna_grid = copy.deepcopy(data)
    antennas = get_antennas(antenna_grid)
    antinode_counter = 0
    for a in antennas:
        for a1 in antennas[a]:
            for a2 in antennas[a]:
                if a1 != a2:
                    antinode_counter += draw_antinodes(a1, a2, antenna_grid)

    print(antinode_counter)


def part2(data):
    antenna_grid = copy.deepcopy(data)
    antennas = get_antennas(antenna_grid)
    antinode_counter = 0
    for a in antennas:
        for a1 in antennas[a]:
            antinode_counter += 1
            for a2 in antennas[a]:
                if a1 != a2:
                    antinode_counter += draw_antinodes(a1, a2, antenna_grid, True)

    print(antinode_counter)


if __name__ == "__main__":
    data = get_input()
    part1(data)
    part2(data)

