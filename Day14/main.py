import re

def get_input():
    with open("input.txt") as f:
        data = f.read().splitlines()
        data_dict = {}
        for i in range(len(data)):
            splitted = data[i].split("v=")
            p = splitted[0].replace("p=", "").split(",")
            p = (int(p[0]), int(p[1]))
            v = splitted[1].split(",")
            v = (int(v[0]), int(v[1]))
            data_dict[i] = (p, v)
        return data_dict


def count_position(r_data, width, height, times):
    starting_p = r_data[0]
    p = starting_p
    v = r_data[1]
    for i in range(times):
        new_y = p[1] + v[1]
        new_x = p[0] + v[0]

        # Teleport to other side if out of bounds
        if new_x < 0:
            new_x = width + new_x
        if new_x >= width:
            new_x = new_x % width
        if new_y < 0:
            new_y = height + new_y
        if new_y >= height:
            new_y = new_y % height

        p = (new_x, new_y)

    return p[0], p[1]


def part1(data, w, h):
    grid = [[0 for _ in range(w)] for _ in range(h)]

    for v in data.values():
        x, y = count_position(v, w, h, 100)
        grid[y][x] += 1

    # Split grid into quadrants and remove middle row
    middle_x = h // 2
    middle_y = w // 2

    grid = grid[:middle_x] + grid[middle_x + 1:]
    grid = [row[:middle_y] + row[middle_y + 1:] for row in grid]
    h -= 1
    w -= 1

    # Split grid into quadrants and count total
    top_left = [grid[i][:w // 2] for i in range(h // 2)]
    top_left_total = sum([sum(row) for row in top_left])
    top_right = [grid[i][w // 2:] for i in range(h // 2)]
    top_right_total = sum([sum(row) for row in top_right])
    bot_left = [grid[i][:w // 2] for i in range(h // 2, h)]
    bot_left_total = sum([sum(row) for row in bot_left])
    bot_right = [grid[i][w // 2:] for i in range(h // 2, h)]
    bot_right_total = sum([sum(row) for row in bot_right])

    # Factor of all quadrants
    print(top_left_total * top_right_total * bot_left_total * bot_right_total)


def part2(data, w, h):
    grid = [[0 for _ in range(w)] for _ in range(h)]
    times = 1
    starting_p = [v[0] for v in data.values()]
    vs = [v[1] for v in data.values()]

    while True:
        for v in range(len(starting_p)):
            r = starting_p[v], vs[v]
            x, y = count_position(r, w, h, 1)
            grid[y][x] = 1
            starting_p[v] = (x, y)

        # Find xmas tree shape
        for r in grid:
            regex = r"1{8,}"
            row = "".join([str(i) for i in r])
            if re.search(regex, row):
                print(times)
                return

        times += 1
        grid = [[0 for _ in range(w)] for _ in range(h)]


if __name__ == "__main__":
    data = get_input()
    part1(data, 101, 103)
    part2(data, 101, 103)
