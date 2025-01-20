def get_input():
    with open("input.txt") as f:
        data = f.read()
        return data.split("\n")


def find_guard_index(data):
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] == "^":
                return x, y


def move_guard(grid, start_x, start_y, direction):
    guard_pos_x = start_x
    guard_pos_y = start_y
    directions = ["up", "right", "down", "left"]

    x_count = 0
    while True:
        # Check if the guard is out of bounds
        if guard_pos_y < 0 or guard_pos_y >= len(grid[0]) or guard_pos_x < 0 or guard_pos_x >= len(grid):
            return grid, False

        # Check if the guard has visited all the cells aka looped
        if x_count == len(grid) * len(grid[0]) - 1:
            return grid, True

        # Count the number of cells visited to check if the guard has looped
        current = grid[guard_pos_x][guard_pos_y]
        if current == 'X':
            x_count += 1

        if grid[guard_pos_x][guard_pos_y] == "#":
            # Return to the previous position
            if direction == "up":
                guard_pos_x += 1
            elif direction == "down":
                guard_pos_x -= 1
            elif direction == "left":
                guard_pos_y += 1
            elif direction == "right":
                guard_pos_y -= 1
            direction = directions[(directions.index(direction) + 1) % 4]
        else:
            grid[guard_pos_x][guard_pos_y] = "X"
        if direction == "up":
            guard_pos_x -= 1
        elif direction == "down":
            guard_pos_x += 1
        elif direction == "left":
            guard_pos_y -= 1
        elif direction == "right":
            guard_pos_y += 1


def part1(data):
    start_x, start_y = find_guard_index(data)
    grid = [list(x) for x in data]

    grid, is_loop = move_guard(grid, start_x, start_y, "up")

    x_count = 0
    for row in grid:
        x_count += row.count("X")

    print(x_count)


def part2(data):
    start_x, start_y = find_guard_index(data)
    grid = [list(x) for x in data]

    loop_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == ".":
                grid[i][j] = "#"
                grid, is_loop = move_guard(grid, start_x, start_y, "up")
                if is_loop:
                    loop_count += 1
                # Reset the grid
                grid = [list(x) for x in data]

    print(loop_count)


if __name__ == "__main__":
    data = get_input()
    part1(data)
    part2(data)
