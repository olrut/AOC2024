def get_input():
    with open("input.txt") as f:
        data = f.read().splitlines()
        int_grid = []
        # Convert to int
        for row in data:
            int_grid.append([int(x) for x in row])
        return int_grid


def find_trailheads(grid):
    trailheads = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 0:
                trailheads.append((x, y))
    return trailheads


def walk_trail(grid, x, y, elevation, end_height, visited_trailends=None, keep_track=True):
    if visited_trailends is None and keep_track:
        visited_trailends = set()

    # Check limits
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        return 0

    if grid[x][y] != elevation:
        return 0

    # Check if trail end is visited
    if keep_track:
        if (x, y) in visited_trailends:
            return 0

    # Check if end height is reached
    if elevation == end_height:
        if keep_track:
            visited_trailends.add((x, y))
        return 1

    # Recursively move to next elevation
    score = (walk_trail(grid, x - 1, y, elevation + 1, end_height, visited_trailends, keep_track) +  # Down
             walk_trail(grid, x + 1, y, elevation + 1, end_height, visited_trailends, keep_track) +  # Up
             walk_trail(grid, x, y - 1, elevation + 1, end_height, visited_trailends, keep_track) +  # Left
             walk_trail(grid, x, y + 1, elevation + 1, end_height, visited_trailends, keep_track))  # Right

    return score


def part1(data):
    end_height = 9
    total_score = 0

    trailheads = find_trailheads(data)
    for h in trailheads:
        x, y = h
        total_score += walk_trail(data, x, y, 0, end_height)

    print(total_score)


def part2(data):
    end_height = 9
    total_score = 0

    trailheads = find_trailheads(data)
    for h in trailheads:
        x, y = h
        total_score += walk_trail(data, x, y, 0, end_height, keep_track=False)

    print(total_score)


if __name__ == "__main__":
    data = get_input()
    part1(data)
    part2(data)
