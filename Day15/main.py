import copy


def get_input():
    with open("input.txt") as f:
        data = f.read().split("\n\n")
        map = data[0].split("\n")
        map = [list(row) for row in map]
        movements = data[1].splitlines()
        movements = [list(movement) for movement in movements]
        return map, movements


def part1(data):
    map = data[0]
    for row in map:
        print("".join(row))
    movements = data[1]
    robot_pos = (0, 0)
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "@":
                robot_pos = (j, i)

    directions = [">", "<", "^", "v"]

    for r in movements:
        for i in r:
            if i == directions[0]:
                move = (0, 1)
                print("Move right")
            if i == directions[1]:
                move = (0, -1)
                print("Move left")
            if i == directions[2]:
                move = (-1, 0)
                print("Move up")
            if i == directions[3]:
                move = (1, 0)
                print("Move down")

            new_pos = (robot_pos[0] + move[0], robot_pos[1] + move[1])

            if map[new_pos[0]][new_pos[1]] == "#":
                print("Hit wall")

            elif map[new_pos[0]][new_pos[1]] == ".":
                map[robot_pos[0]][robot_pos[1]] = "."
                map[new_pos[0]][new_pos[1]] = "@"
                robot_pos = new_pos

            else:  # Is 0
                finder_pos = (robot_pos[0] + move[0] + move[0], robot_pos[1] + move[1] + move[1])
                while True:
                    if map[finder_pos[0]][finder_pos[1]] == "#":
                        break
                    if map[finder_pos[0]][finder_pos[1]] == "O":
                        finder_pos = (finder_pos[0] + move[0], finder_pos[1] + move[1])

                    if map[finder_pos[0]][finder_pos[1]] == ".":
                        map[finder_pos[0]][finder_pos[1]] = "O"
                        map[robot_pos[0]][robot_pos[1]] = "."
                        map[new_pos[0]][new_pos[1]] = "@"
                        robot_pos = new_pos
                        break

        for row in map:
            print("".join(row))

        counter = 0
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == "O":
                    counter += 100 * i + j

        print(counter)

def get_boxes(map, pos, dir):
    pass
    # TODO

def part2(data):
    map = data[0]

    double_map = [[] for _ in map[0]]

    # If the tile is #, the new map contains ## instead.
    # If the tile is O, the new map contains [] instead.
    # If the tile is ., the new map contains .. instead.
    # If the tile is @, the new map contains @. instead.

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "#":
                double_map[i].append("#")
                double_map[i].append("#")
            elif map[i][j] == "O":
                double_map[i].append("[")
                double_map[i].append("]")
            elif map[i][j] == ".":
                double_map[i].append(".")
                double_map[i].append(".")
            elif map[i][j] == "@":
                double_map[i].append("@")
                double_map[i].append(".")

    for row in double_map:
        print("".join(row))

    movements = data[1]
    robot_pos = (0, 0)
    for i in range(len(double_map)):
        for j in range(len(double_map[i])):
            if double_map[i][j] == "@":
                robot_pos = (i, j)

    directions = [">", "<", "^", "v"]

    for r in movements:
        for i in r:
            if i == directions[0]:
                move = (0, 1)
                print("Move right")
            if i == directions[1]:
                move = (0, -1)
                print("Move left")
            if i == directions[2]:
                move = (-1, 0)
                print("Move up")
            if i == directions[3]:
                move = (1, 0)
                print("Move down")

            new_pos = (robot_pos[0] + move[0], robot_pos[1] + move[1])

            if double_map[new_pos[0]][new_pos[1]] == "#":
                print("Hit wall")

            elif double_map[new_pos[0]][new_pos[1]] == ".":
                double_map[robot_pos[0]][robot_pos[1]] = "."
                double_map[new_pos[0]][new_pos[1]] = "@"
                robot_pos = new_pos

            else:  # Is [ or ]
                boxes = get_boxes(double_map, robot_pos, move)

            for row in double_map:
                print("".join(row))




if __name__ == "__main__":
    data = get_input()
    # part1(data)
    copy = copy.deepcopy(data)
    part2(data)
