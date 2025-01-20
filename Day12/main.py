import copy


def get_input():
    with open("input.txt") as f:
        data = f.read().splitlines()
        char_grid = []
        for row in data:
            char_grid.append(list(row))
        return char_grid


def count_fence(data, x, y, current, marker):
    n_count = 0
    fence_count = 0
    data[x][y] = marker
    n_count += 1
    # Up out of bound
    if x - 1 < 0:
        fence_count += 1
    # Up not same and not marker
    elif data[x - 1][y] != current and data[x - 1][y] != marker:
        fence_count += 1
    # Up same
    elif data[x - 1][y] == current:
        a, n = count_fence(data, x - 1, y, current, marker)
        fence_count += a
        n_count += n
    # Down out of bound
    if x + 1 >= len(data):
        fence_count += 1
    # Down not same and not marker
    elif data[x + 1][y] != current and data[x + 1][y] != marker:
        fence_count += 1
    # Down same
    elif data[x + 1][y] == current:
        a, n = count_fence(data, x + 1, y, current, marker)
        fence_count += a
        n_count += n
    # Left out of bound
    if y - 1 < 0:
        fence_count += 1
    # Left not same
    elif data[x][y - 1] != current and data[x][y - 1] != marker:
        fence_count += 1
    # Left same
    elif data[x][y - 1] == current:
        a, n = count_fence(data, x, y - 1, current, marker)
        fence_count += a
        n_count += n
    # Right out of bound
    if y + 1 >= len(data[x]):
        fence_count += 1
    # Right not same and not marker
    elif data[x][y + 1] != current and data[x][y + 1] != marker:
        fence_count += 1
    # Right same
    elif data[x][y + 1] == current:
        a, n = count_fence(data, x, y + 1, current, marker)
        fence_count += a
        n_count += n
    return fence_count, n_count


def count_corners(data, x, y, current, marker):
    n_count = 0
    corner_count = 0
    data[x][y] = marker  # Mark the cell as visited
    n_count += 1

    # Bound check
    def in_bounds(x, y):
        return 0 <= x < len(data) and 0 <= y < len(data[0])

    # Check for corners
    directions = [
        (-1, -1), (-1, 1), (1, 1), (1, -1)
    ]

    for dx, dy in directions:
        corner_x, corner_y = x + dx, y + dy
        side1_x, side1_y = x + dx, y
        side2_x, side2_y = x, y + dy

        # Both out of bounds
        if not in_bounds(side1_x, side1_y) and not in_bounds(side2_x, side2_y):
            corner_count += 1  # Count as a corner if both sides are out of bounds
            continue


        # One side is out of bounds and other is same or marker
        if not in_bounds(side1_x, side1_y):
            if data[side2_x][side2_y] != current and data[side2_x][side2_y] != marker:
                corner_count += 1
        if not in_bounds(side2_x, side2_y):
            if data[side1_x][side1_y] != current and data[side1_x][side1_y] != marker:
                corner_count += 1


        # Both sides are in bounds and not same or marker
        if in_bounds(side1_x, side1_y) and in_bounds(side2_x, side2_y):
            if data[side1_x][side1_y] != current and data[side1_x][side1_y] != marker and data[side2_x][side2_y] != current and data[side2_x][side2_y] != marker:
                corner_count += 1

            # Inner corners
            # Both sides are in bounds and same and corner is different
            if (data[side1_x][side1_y] == current or data[side1_x][side1_y] == marker) and (data[side2_x][side2_y] == current or data[side2_x][side2_y] == marker):
                if data[corner_x][corner_y] != current and data[corner_x][corner_y] != marker:
                    corner_count += 1
                    continue

    # Check for connected cells in 4 directions
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if in_bounds(nx, ny) and data[nx][ny] == current and data[nx][ny] != marker:
            sub_corner_count, sub_n_count = count_corners(data, nx, ny, current, marker)
            corner_count += sub_corner_count
            n_count += sub_n_count

    return corner_count, n_count


def part1(data):
    total_price = 0
    marker = 0
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            region = data[i][j]

            # if region is char, count the region
            if isinstance(region, int):
                continue

            fence, n = count_fence(data, i, j, data[i][j], marker)
            total_price += fence * n
            marker += 1
    print(total_price)


def part2(data):
    total_price = 0
    marker = 0
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            region = data[i][j]

            # If region is char, count the region
            if isinstance(region, int):
                continue

            corner, n = count_corners(data, i, j, data[i][j], marker)
            total_price += corner * n
            marker += 1

    print(total_price)


if __name__ == "__main__":
    data = get_input()
    part1(copy.deepcopy(data))
    part2(copy.deepcopy(data))