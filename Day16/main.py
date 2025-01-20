import heapq

def get_input():
    with open("input.txt") as f:
        data = f.read().splitlines()
        grid = []
        for row in data:
            grid.append(list(row))
        return grid


def dijkstra(grid, start, end):
    directions = [
        (0, 1),  # Right
        (-1, 0),  # Down
        (0, -1),  # Left
        (1, 0)  # Up
    ]

    # Initialize distances and parents
    distances = {(i, j): float('inf') for i in range(len(grid)) for j in range(len(grid[i]))}
    distances[start] = 0
    parents = {}

    queue = [(0, start, (0, 1))]

    # Set of visited nodes
    visited = set()

    while queue:
        current_distance, current_node, previous_direction = heapq.heappop(queue)

        if current_node in visited:
            continue

        if current_node == end:
            break

        visited.add(current_node)

        # Visit neighbors
        for direction in directions:
            neighbor = (current_node[0] + direction[0], current_node[1] + direction[1])

            # If the neighbor is outside the grid, skip it
            if grid[neighbor[0]][neighbor[1]] == "#":
                continue

            # Count the new distance
            new_distance = current_distance + 1

            # If the direction has changed, add 1000
            if direction != previous_direction:
                new_distance += 1000

            # Update the distance if the new distance is smaller
            if new_distance <= distances[neighbor]:
                distances[neighbor] = new_distance
                parents[neighbor] = current_node
                heapq.heappush(queue, (new_distance, neighbor, direction))

    path = []
    current = end
    while current in parents:
        path.append(current)
        current = parents[current]
    path.append(start)
    path.reverse()

    return distances[end], path


def part1(data):
    start = (0, 0)
    end = (0, 0)

    # Etsi start- ja end-koordinaatit
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "S":
                start = (i, j)
            if data[i][j] == "E":
                end = (i, j)

    dist, path = dijkstra(data, start, end)

    for i in range(len(data)):
        for j in range(len(data[i])):
            if (i, j) in path:
                data[i][j] = "X"

    for row in data:
        print("".join(row))

    print()
    print(len(path))

def part2(data):
    # TODO: Implement part2
    pass


if __name__ == "__main__":
    data = get_input()
    part1(data)